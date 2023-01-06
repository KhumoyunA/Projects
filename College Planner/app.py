# -*- coding: utf-8 -*-
"""
 Planner
=======
    : Original flaskr code: Copyright (c) 2015 by Armin Ronacher and contributors
    :license: BSD, see LICENSE for more details.
    :reference: Flaskr project from CS253, code provided by Mark Liffiton
"""

import os
from sqlite3 import dbapi2 as sqlite3
import werkzeug
from flask import Flask, session, request, g, redirect, url_for, render_template, flash
from dateutil.parser import parse
from datetime import datetime, time
from datetime import timedelta
from datetime import date
from flask_mail import Mail, Message
import random
import string

# create our little application :)
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "collegeplanner2022@gmail.com"
app.config['MAIL_PASSWORD'] = "trrokwsvssunosar"
app.config['MAIL_DEFAULT_SENDER'] = "collegeplanner2022@gmail.com"
mail = Mail(app)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'planner.db'),
    DEBUG=True,
    SECRET_KEY='06c542065867863bac55dccdc883fa46fed7c151',
))
# may have to change
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def show_tasks():
    """Shows all entries, optionally filtered by category, with
    a category selection interface and add post interface above.
    """
    db = get_db()

    if not session.get('logged_in'):
        return render_template('welcome_page.html')
    else:
        input_category = request.args.get('category')
        # Filter view if category specified in query string
        if input_category is not None and input_category != 'All':
            cur = db.execute(
                'SELECT * FROM events WHERE UPPER(category) = ? AND user_id = ? ORDER BY en_date, en_time DESC',
                [(input_category), session.get('user_id')])
            tasks = cur.fetchall()
        else:
            cur = db.execute('SELECT * FROM events WHERE user_id = ? ORDER BY en_date, en_time DESC',
                             [session.get('user_id')])
            tasks = cur.fetchall()

        # Get a list of categories for populating the category chooser
        cur = db.execute('SELECT DISTINCT UPPER(category) AS category FROM events WHERE category NOT LIKE "" ORDER BY '
                         'id desc')
        categories = cur.fetchall()

    return render_template('show_events.html', tasks=tasks, categories=categories, todos=get_todo(),
                           reminders=get_reminder(), titles=search_suggestions(input_category), name=get_name())


def get_categories():
    """A method that fetches all categories in the database. Used as a helper function to make sure filter posts
      has access to categories regardless of the page
    """
    db = get_db()
    cur = db.execute('SELECT DISTINCT UPPER(category) AS category FROM events WHERE category NOT LIKE "" ORDER BY '
                     'id desc')
    categories = cur.fetchall()
    return categories


@app.route('/add', methods=['POST'])
def add_entry():
    """Adds a new event"""
    db = get_db()
    times = request.form['repeat_frequency']
    db.execute('INSERT INTO events (title, category, st_date, st_time, en_date, en_time, description, user_id) '
               'VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
               [request.form['title'], request.form['category'], request.form['st_date'],
                request.form['st_time'], request.form['en_date'], request.form['en_time'], request.form['description'],
                session.get('user_id')])
    if times != "":
        time_now = request.form['st_date']
        month = int(time_now[:2])
        day = int(time_now[3:5])
        year = int(time_now[6:])
        chosen_date = date(year, month, day)
        time_delta = timedelta(days=1)

        for i in range(int(times)):
            time_new = chosen_date + time_delta
            chosen_date = time_new
            time_new = time_new.strftime("%m/%d/%Y")
            db.execute('INSERT INTO events (title, category, st_date, st_time, en_date, en_time, description) '
                       'VALUES (?, ?, ?, ?, ?, ?, ?)',
                       [request.form['title'], request.form['category'], time_new,
                        request.form['st_time'], time_new, request.form['en_time'],
                        request.form['description']])
    db.commit()
    flash('New event was successfully posted!')
    return redirect(url_for('show_tasks'))


@app.route('/delete', methods=['POST'])
def delete_entry():
    """Deletes a selected event, identified by its id"""
    db = get_db()
    db.execute('DELETE FROM events WHERE id=?', [request.form['id']])
    db.commit()
    flash('Event deleted!')
    return redirect(url_for('show_tasks'))


@app.route('/check_entry', methods=['POST'])
def check_entry():
    """Sets the event with matching id to have checked status"""
    db = get_db()
    db.execute("UPDATE events SET check_status = 'event_planner_checked' WHERE id = ?", [request.form['id']])
    db.commit()
    return redirect(url_for('show_tasks'))


@app.route('/uncheck_entry', methods=['POST'])
def uncheck_entry():
    """Sets the event with matching id to have unchecked status"""
    db = get_db()
    db.execute("UPDATE events SET check_status = 'event_planner_unchecked' WHERE id = ?", [request.form['id']])
    db.commit()
    return redirect(url_for('show_tasks'))


@app.route('/suggest-add')
def suggest_add():
    """Renders the page to the add task page upon button click"""
    return render_template('add_task.html', todos=get_todo())


@app.route('/add-todo', methods=['POST'])
def add_todo():
    """Adds a new to do"""
    db = get_db()
    desc = request.form['description']

    # check that to-do is not blank
    if desc != "":
        db.execute('INSERT INTO todos (description) VALUES (?)', [request.form['description']])
        db.commit()

    return redirect('/#todo')


@app.route('/delete-todo', methods=['POST'])
def delete_todo():
    """Deletes a selected todo, identified by its id"""
    db = get_db()
    f = request.form

    if request.form:
        for item in f.getlist('id'):
            db.execute('DELETE FROM todos WHERE id=?', [item])
            db.commit()
        flash('Todo(s) Completed!')
    return redirect(url_for('show_tasks'))


def get_todo():
    """
    Returns all todos in the todos table. It is used as a helper function to pass todos for rendering
    :return: todos
    """
    db = get_db()
    cur = db.execute('SELECT * FROM todos ORDER BY id ASC')
    todos = cur.fetchall()
    return todos


@app.route('/suggest-settings')
def suggest_settings():
    """Renders the page to show settings upon button click"""
    return render_template('settings.html', categories=get_categories())


@app.route('/login_settings')
def login_settings():
    """Renders the page to show log in page upon button click"""
    return render_template('login.html')


@app.route('/create_account')
def create_account():
    """Renders the page to show create account page upon button click"""
    return render_template('create_account.html')


@app.route('/edit', methods=['GET'])
def edit_entry():
    """Fetch the post for editing, identified by its id"""
    db = get_db()
    cur = db.execute('SELECT * FROM events WHERE id = ?',
                     [request.args.get('id')])
    task = cur.fetchone()
    return render_template('edit_event.html', task=task)


@app.route('/update', methods=['POST'])
def update_entry():
    """Update the post content, identified by its id"""
    db = get_db()
    db.execute('UPDATE events SET title = ?, category = ?, st_date = ?, st_time = ?, en_date = ?, en_time = ?, '
               'description = ? WHERE id = ?',
               [request.form['title'], request.form['category'], request.form['st_date'], request.form['st_time'],
                request.form['en_date'], request.form['en_time'], request.form['description'], request.form['id']])
    db.commit()
    flash('Event updated!')
    return redirect(url_for('show_tasks'))


@app.route('/filter-date', methods=['GET'])
def filter_date():
    """Show only events that are due on an input date"""
    db = get_db()
    cur = db.execute('SELECT * FROM events WHERE st_date = ?',
                     [request.args.get('date')])
    db.commit()
    tasks = cur.fetchall()
    return render_template('filter_view.html', tasks=tasks, todos=get_todo(), date=request.args.get('date'))


@app.route('/search', methods=['GET'])
def search_entries():
    """Find an entry based on search term"""
    db = get_db()

    cur = db.execute('SELECT * FROM events WHERE title = ?',
                     [request.args['search']])
    db.commit()

    tasks = cur.fetchall()
    return render_template('filter_view.html', tasks=tasks, todos=get_todo(), search=request.args['search'])


def search_suggestions(cat):
    """Curate search suggestions based on titles that are shown on show_events"""
    db = get_db()
    db.row_factory = lambda cursor, row: row[0]  # got this from Evan :)
    c = db.cursor()

    # check if there is a category
    if cat != None:
        cur = c.execute('SELECT title FROM events WHERE category = ? GROUP BY title',
                        [cat])
    else:
        cur = c.execute('SELECT title FROM events GROUP BY title')

    titles = cur.fetchall()
    return titles


@app.route('/create_account_submit', methods=['POST'])
def create_account_submit():

    # If the entered password, username or email is an empty string, makes the user try again:
    if request.form['password'] == '' \
            or request.form['user_name'] == '' \
            or request.form['email_addr'] == '':
        flash('Error: Please fill out all fields.')
        return(render_template('create_account.html'))

    # Check if entered username is already in database
    db = get_db()
    cur = db.execute('SELECT * FROM users WHERE user_name = ?',
                        [request.form['user_name']])
    if len(cur.fetchall()) > 0:
        flash('Error: Username already taken.')
        return (render_template('create_account.html'))

    else:
        # Creates an account with the submitted fields and puts it in events table
        password = request.form['password']
        hashed_pass = werkzeug.security.generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
        db = get_db()
        db.execute('INSERT INTO users (first_name, last_name, email_addr, user_name, user_hash) ' 
                   'VALUES (?, ?, ?, ?, ?)',
                   [request.form['first_name'], request.form['last_name'], request.form['email_addr'],
                    request.form['user_name'], hashed_pass])
        db.commit()
        flash('Account Created!')
        return redirect(url_for('login_settings'))


@app.route('/login', methods=['POST'])
def login():
    # Logs the user into the website with correct username and password

    db = get_db()

    # Got information about Count() in SQLite from SQLiteTutorial: https://www.sqlitetutorial.net/sqlite-count-function/

    # Retrieves how many rows are in users table with matching username from form
    cur = db.execute('SELECT COUNT(*) FROM users WHERE user_name=?', [request.form['user_name']])

    # if the username exists:
    if cur.fetchall()[0][0] > 0:

        # Get hashed password from db
        cur = db.execute('SELECT user_hash FROM users WHERE user_name=?', [request.form['user_name']])
        password_hashed = cur.fetchone()['user_hash']

        # If the entered password matches with hashed password:
        if werkzeug.security.check_password_hash(password_hashed, request.form['password']):

            # Logs the user in
            session['logged_in'] = True

            # Gets user's id and assigns it to session['user_id']
            cur = db.execute('SELECT user_id FROM users WHERE user_name=?', [request.form['user_name']])
            session['user_id'] = cur.fetchone()['user_id']
            
            flash('You were logged in!')
            return redirect(url_for('show_tasks'))
        else:
            flash('Incorrect Password')
            return render_template('login.html')
    else:
        flash('Username not found, please try again')
        return render_template('login.html')


@app.route('/check_todo', methods=['POST'])
def check_todo():
    db = get_db()
    db.execute("UPDATE todos SET status = 'todo_checked' WHERE id = ?", [request.form['id']])
    db.commit()
    flash('Todo Checked!')
    return redirect(url_for('show_tasks'))


@app.route('/uncheck_todo', methods=['POST'])
def uncheck_todo():
    db = get_db()
    db.execute("UPDATE todos SET status = 'todo_unchecked' WHERE id = ?", [request.form['id']])
    db.commit()
    flash('Todo Unchecked!')
    return redirect(url_for('show_tasks'))


def get_reminder():
    """
    Returns all reminders
    :return: reminders
    """
    current_time = datetime.now()
    today_date = current_time.strftime('%m/%d/%Y')
    db = get_db()
    cur = db.execute('SELECT title FROM events WHERE en_date = ?', [today_date])
    reminders = cur.fetchall()
    return reminders


@app.route('/logout')
def logout():
    # Logs the user out of the website
    session['logged_in'] = False
    flash('You were logged out')
    return render_template('login.html')


def get_name():
    db = get_db()
    cur = db.execute('SELECT first_name FROM users WHERE user_id = ?',
                     [session.get('user_id')])
    first_name = cur.fetchone()
    return first_name


def send_email(email, rand_str):
    """
`    Sends an email with a randon string (for verification) to the given user's email address
    :param email: user's email address
    :param rand_str: a random string generated by another method ato verify the user
    """
    msg = Message("College Planner Password Reset", sender=app.config["MAIL_DEFAULT_SENDER"], recipients=[email])
    msg.html = render_template('reset_email.html', rand_str=rand_str)
    mail.send(msg)


@app.route('/reset-password')
def render_reset():
    """Renders the page to show reset password page upon button click"""
    return render_template('request_reset.html')


@app.route('/request_reset', methods=["GET", "POST"])
def request_reset():
    """
    Renders the request reset page where the user inputs their email address. If the email address is in our database,
    then the user receives a reset email
    :return: redirect to login_settings page
    """
    db = get_db()
    email = request.form["email"]
    cur = db.execute('SELECT email_addr FROM users WHERE email_addr = ?', [email])
    email1 = cur.fetchone()
    if email1 != None:
        rand_str = generate_rand_str(email)
        send_email(email, rand_str)
    flash("If the entered email address is registered with us, you will receive an email with a reset link.")
    return redirect(url_for('login_settings'))


def generate_rand_str(email):
    """
    Generates a random string of length 5 and saves it in the database for that particular user
    :param email: email address of the user who requested a password reset
    :return:random string
    """
    db = get_db()
    random_s = ''.join(random.choices(string.ascii_lowercase, k=5))
    cur = db.execute('UPDATE users SET random_string = ?  WHERE email_addr = ?', [random_s, email])
    db.commit()
    return random_s


def verify_string(rand_str):
    """
    Verifies that the user string is a valid one tied to a user in the database
    :param: a random string to verify
    :return:a boolean indicating if the string is valid or not
    """
    db = get_db()
    cur = db.execute('SELECT user_id FROM users WHERE random_string = ?', [rand_str])
    user_string = cur.fetchone()

    if user_string != None:
        return True
    return False


@app.route('/string_verified/<rand_str>')
def string_verified(rand_str):
    """
    Once string is verified , it renders reset_password page where the user can enter a new password
    :param: a random string
    :return:   renders template reset_password
    """
    db = get_db()
    cur = db.execute('SELECT email_addr FROM users WHERE random_string =?', [rand_str])
    email = cur.fetchone()
    email_string = ''
    # get the email in the string form
    for e_mail in email:
        email_string = e_mail
    if verify_string(rand_str):
        return render_template('reset_password.html', email_string=email_string)


@app.route('/set-password', methods=['POST'])
def set_password():
    """
    Allows the user to set a new password
    :return:redirects the user to login page
    """
    db = get_db()
    password = request.form["password"]
    email = request.form["email"]
    hashed_pass = werkzeug.security.generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
    cur = db.execute('UPDATE users SET user_hash = ? WHERE email_addr = ?', [hashed_pass, email])
    db.commit()
    flash("You have successfully reset your password!")
    return redirect(url_for("login_settings"))


@app.route('/')
def render_main():
    """
    Renders welcome page
    """
    return render_template('welcome_page.html')
