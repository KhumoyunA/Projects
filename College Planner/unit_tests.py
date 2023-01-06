import os
import app as flaskr
import unittest
import tempfile
from dateutil.parser import parse
from datetime import datetime
from datetime import timedelta
import datetime
from datetime import date


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.testing = True
        self.app = flaskr.app.test_client()
        with flaskr.app.app_context():
            flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

    def create_account(self, first_name, last_name, email_addr, user_name, password):
        # define function for creating account
        return self.app.post('/create_account_submit', data=dict(
            first_name=first_name,
            last_name=last_name,
            email_addr=email_addr,
            user_name=user_name,
            password=password
        ), follow_redirects=True)

    def login(self, user_name, password):
        # define function for logging into the account
        return self.app.post('/login', data=dict(
            user_name=user_name,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_create_account(self):
        rv = self.create_account('Tommy', 'Titan', 'ttitan@iwu.edu', 'admin', 'default')
        assert b'Account Created!' in rv.data

    def test_login_and_logout(self):
        rv = self.create_account('Tommy', 'Titan', 'ttitan@iwu.edu', 'admin', 'default')
        assert b'Account Created!' in rv.data

        rv = self.login('admin', 'default')

        assert b'You were logged in' in rv.data
        assert b'You were logged out' not in rv.data

        rv = self.logout()

        assert b'You were logged out' in rv.data
        assert b'You were logged in' not in rv.data

    def test_empty_db(self):
        # unit test for asserting that the database is empty

        self.create_account('Tommy', 'Titan', 'ttitan@iwu.edu', 'admin', 'default')
        self.login('admin', 'default')

        rv = self.app.get('/')
        assert b'No tasks so far' in rv.data

    def test_messages(self):
        # unit test for adding post and making sure the database is NOT empty

        # create account and login to the account
        self.create_account('Tommy', 'Titan', 'ttitan@iwu.edu', 'admin', 'default')
        self.login('admin', 'default')

        rv = self.app.post('/add', data=dict(
            title='Reading',
            category='CS253',
            st_date='10/28/2022',
            st_time='10:00 AM',
            en_date='10/29/2022',
            en_time='11:00 AM',
            repeat_frequency='0',
            description='Data types and login information'

        ), follow_redirects=True)

        # assert database is not empty
        assert b'No tasks so far' not in rv.data

        # assert the content from the entry is added
        assert b'Reading' in rv.data
        assert b'CS253' in rv.data
        assert b'10/28/2022' in rv.data
        assert b'10:00 AM' in rv.data

    def test_delete_messages(self):
        # unit test for deleting a post after adding it
        self.create_account('Tommy', 'Titan', 'ttitan@iwu.edu', 'admin', 'default')
        self.login('admin', 'default')

        rv = self.app.post('/add', data=dict(
            id=1,
            title='Science',
            category='STEM',
            st_date='10/28/2022',
            st_time='10:00 AM',
            en_date='10/28/2022',
            en_time='12:00 PM',
            repeat_frequency='0',
            description='Test today'
        ))
        rv = self.app.post('/add', data=dict(
            id=2,
            title='WebDev',
            category='NoCS',
            st_date='10/08/2022',
            st_time='10:00 AM',
            en_date='11/28/2022',
            en_time='12:00 PM',
            repeat_frequency='0',
            description='Assignment due'
        ))
        rv = self.app.post('/add', data=dict(
            id=3,
            title='NewSc',
            category='Formula',
            st_date='10/28/2022',
            st_time='10:00 AM',
            en_date='10/28/2022',
            en_time='12:00 PM',
            repeat_frequency='0',
            description='Exam after two weeks'
        ))

        assert b'No tasks so far' not in rv.data

        # delete the event where id = 1
        rv = self.app.post('/delete', data=dict(
            id=1
        ), follow_redirects=True)

        # assert entry for id = 1 is deleted
        assert b'Science' not in rv.data
        assert b'STEM' not in rv.data

        # assert all other entries are still there
        assert b'WebDev' in rv.data
        assert b'NoCS' in rv.data
        assert b'NewSc' in rv.data
        assert b'Formula' in rv.data

    def test_filter_message(self):
        # unit test for filtering post by category
        self.create_account('Tommy', 'Titan', 'ttitan@iwu.edu', 'admin', 'default')
        self.login('admin', 'default')

        rv = self.app.post('/add', data=dict(
            id=1,
            title='Geometry',
            category='Math',
            st_date='10/28/2022',
            st_time='10:00 AM',
            en_date='10/28/2022',
            en_time='12:00 AM',
            repeat_frequency='0',
            description='Assignment due'
        ))
        rv = self.app.post('/add', data=dict(
            id=2,
            title='Social',
            category='Mind',
            st_date='10/28/2022',
            st_time='10:00 AM',
            en_date='10/28/2022',
            en_time='12:00 AM',
            repeat_frequency='0',
            description='View lecture recording'
        ))
        rv = self.app.post('/add', data=dict(
            id=3,
            title='Cognitive',
            category='Mind',
            st_date='10/23/2022',
            st_time='10:00 AM',
            en_date='10/23/2022',
            en_time='12:00 AM',
            repeat_frequency='0',
            description='Meeting in CNS210'
        ))
        rv = self.app.post('/add', data=dict(
            id=4,
            title='Rats',
            category='Study',
            st_date='10/23/2022',
            st_time='10:00 AM',
            en_date='10/23/2022',
            en_time='12:00 AM',
            repeat_frequency='0',
            description='Lab in basement'
        ))
        assert b'No tasks so far' not in rv.data

        # filter by category
        rv = self.app.get('/?category=MIND')

        assert b'Mind' in rv.data
        assert b'Cognitive' in rv.data
        assert b'Social' in rv.data
        assert b'Rats' not in rv.data
        assert b'Geometry' not in rv.data

        # redirect to the main page
        rv = self.app.get('/')
        assert b'Mind' in rv.data
        assert b'Cognitive' in rv.data
        assert b'Social' in rv.data
        assert b'Rats' in rv.data
        assert b'Geometry' in rv.data
        assert b'Study' in rv.data

    def test_edit_message(self):
        # unit test for editing and updating post content
        self.create_account('Tommy', 'Titan', 'ttitan@iwu.edu', 'admin', 'default')
        self.login('admin', 'default')

        rv = self.app.post('/add', data=dict(
            id=1,
            title='Nothing',
            category='Something',
            st_date='10/23/2022',
            st_time='10:00 AM',
            en_date='10/23/2022',
            en_time='12:00 AM',
            repeat_frequency='0',
            description='Assignment due'
        ))
        rv = self.app.post('/add', data=dict(
            id=2,
            title='Food',
            category='Cook',
            st_date='10/23/2022',
            st_time='10:00 AM',
            en_date='10/23/2022',
            en_time='12:00 AM',
            repeat_frequency='0',
            description='This is due'
        ))

        assert b'No tasks so far' not in rv.data

        # edit the event where id = 1
        rv = self.app.get('/edit', data=dict(
            id=1
        ))

        # assert the values for title and category are stored
        assert b'title="Nothing"'
        assert b'category="Something"'

        # update the information
        rv = self.app.post('/update', data=dict(
            id=1,
            title='New Things',
            category='CSLove',
            st_date='10/23/2022',
            st_time='10:00 AM',
            en_date='10/23/2022',
            en_time='12:00 AM',
            repeat_frequency='0',
            description='Iteration report is due'
        ), follow_redirects=True)

        # assert the updated information is displayed
        assert b'New Things' in rv.data
        assert b'CSLove' in rv.data
        assert b'Food' in rv.data
        assert b'Cook' in rv.data
        assert b'Nothing' not in rv.data
        assert b'Something' not in rv.data

    def test_delete_edge_case(self):
        # unit test for deleting the last post in database
        self.create_account('Tommy', 'Titan', 'ttitan@iwu.edu', 'admin', 'default')
        self.login('admin', 'default')

        rv = self.app.post('/add', data=dict(
            id=1,
            title='NewSc',
            category='Formula',
            st_date='10/23/2022',
            st_time='10:00 AM',
            en_date='10/23/2022',
            en_time='12:00 AM',
            repeat_frequency='0',
            description='New assignment posted'
        ))

        assert b'No tasks so far' not in rv.data

        rv = self.app.post('/delete', data=dict(
            id=1
        ), follow_redirects=True)

        # assert entry for id=1 is deleted and the database is empty
        assert b'No tasks so far' in rv.data
        assert b'NewSc' not in rv.data

    def test_filter_edge_case(self):
        # unit test for filtering post and deleting it
        self.create_account('Tommy', 'Titan', 'ttitan@iwu.edu', 'admin', 'default')
        self.login('admin', 'default')

        rv = self.app.post('/add', data=dict(
            id=1,
            title='Geometry',
            category='Math',
            st_date='10/23/2022',
            st_time='10:00 AM',
            en_date='10/23/2022',
            en_time='12:00 AM',
            repeat_frequency='0',
            description='Nothing is due'
        ))
        rv = self.app.post('/add', data=dict(
            id=2,
            title='Social',
            category='Mind',
            st_date='10/23/2022',
            st_time='10:00 AM',
            en_date='10/23/2022',
            en_time='12:00 AM',
            repeat_frequency='0',
            description='Midterm exam'
        ))
        rv = self.app.post('/add', data=dict(
            id=3,
            title='Rats',
            category='Study',
            st_date='10/23/2022',
            st_time='10:00 AM',
            en_date='10/23/2022',
            en_time='12:00 PM',
            repeat_frequency='0',
            description='Quiz due'
        ))

        assert b'No tasks so far' not in rv.data

        # filter by category
        rv = self.app.get('/?category=MIND')

        assert b'Mind' in rv.data
        assert b'Social' in rv.data
        assert b'Rats' not in rv.data
        assert b'Geometry' not in rv.data

        # delete entry from the filtered page
        rv = self.app.post('/delete', data=dict(
            id=2
        ), follow_redirects=True)

        assert b'Social' not in rv.data
        assert b'Rats' in rv.data
        assert b'Geometry' in rv.data

    def test_todos(self):
        # unit test for adding a to-do and making sure the database is NOT empty
        self.create_account('Tommy', 'Titan', 'ttitan@iwu.edu', 'admin', 'default')
        self.login('admin', 'default')

        rv = self.app.post('/add-todo', data=dict(
            description='Wash the dishes',
        ), follow_redirects=True)

        # assert database is not empty
        assert b'No todos so far' not in rv.data
        # assert the content from the entry is added
        assert b'Wash the dishes' in rv.data

    def test_delete_todos(self):
        # unit test for deleting a to-do after adding it
        self.create_account('Tommy', 'Titan', 'ttitan@iwu.edu', 'admin', 'default')
        self.login('admin', 'default')

        rv = self.app.post('/add-todo', data=dict(
            id=1,
            description='Wash the dishes',
        ))
        rv = self.app.post('/add-todo', data=dict(
            id=2,
            description='Pay rent',
        ))
        rv = self.app.post('/add-todo', data=dict(
            id=3,
            description='Fix the door',
        ))
        rv = self.app.post('/add-todo', data=dict(
            id=4,
            description='Have a date with Ali',
        ))

        assert b'No tasks so far' not in rv.data

        # delete a to-do with id = 1
        rv = self.app.post('/delete-todo', data=dict(
            id=1
        ), follow_redirects=True)

        # assert to do with id=1 is deleted
        assert b'Wash the dishes' not in rv.data

        # assert other to-do tasks are still there
        assert b'Pay rent' in rv.data
        assert b'Fix the door' in rv.data
        assert b'Have a date with Ali' in rv.data

    def test_date_filter_none(self):
        """Unit test for attempting to filter by date with no posts with that date"""
        self.create_account('Tommy', 'Titan', 'ttitan@iwu.edu', 'admin', 'default')
        self.login('admin', 'default')

        rv = self.app.post('/add', data=dict(
            id=1,
            title='Reading',
            description='Data types and login information',
            category='355',
            st_date='12/12/2222',
            st_time='10:22 AM',
            en_date='12/12/2222',
            en_time='10:22 AM',
            repeat_frequency='0'
        ), follow_redirects=True)

        # assert that data is now in the database
        assert b'Reading' in rv.data
        assert b'No tasks so far' not in rv.data

        # select a date
        rv = self.app.get('/filter-date?date=2222%2F09%2F09')

        # assert that no tasks appear
        assert b'No results' in rv.data

    def test_date_filter(self):
        """Test the date filter given that the date is present"""
        self.create_account('Tommy', 'Titan', 'ttitan@iwu.edu', 'admin', 'default')
        self.login('admin', 'default')
        # add an event

        rv = self.app.post('/add', data=dict(
            id=1,
            title='Reading',
            description='Data types and login information',
            category='355',
            st_date='12/12/2222',
            st_time='10:22 AM',
            en_date='12/12/2222',
            en_time='10:22 AM',
            repeat_frequency='0'
        ), follow_redirects=True)
        rv = self.app.post('/add', data=dict(
            id=2,
            title='HW 1',
            description='Data types and login information',
            category='355',
            st_date='08/18/2222',
            st_time='10:22 AM',
            en_date='09/19/2222',
            en_time='10:22 AM',
            repeat_frequency='0'
        ), follow_redirects=True)
        rv = self.app.post('/add', data=dict(
            id=3,
            title='Study',
            description='First homework assignment',
            category='356',
            st_date='09/05/2022',
            st_time='10:22 AM',
            en_date='09/19/2222',
            en_time='10:22 AM',
            repeat_frequency='0'
        ), follow_redirects=True)

        # assert all events are in database
        assert b'HW 1' in rv.data
        assert b'Reading' in rv.data
        assert b'Study' in rv.data

        # select a date
        rv = self.app.get('/filter-date?date=08%2F18%2F2222')

        # assert that only the filtered event appears
        assert b'HW 1' in rv.data

    def test_search(self):
        """Test that search by title works"""
        # add an event
        self.create_account('Tommy', 'Titan', 'ttitan@iwu.edu', 'admin', 'default')
        self.login('admin', 'default')

        rv = self.app.post('/add', data=dict(
            id=1,
            title='Reading',
            description='Data types and login information',
            category='355',
            st_date='12/12/2222',
            st_time='10:22 AM',
            en_date='12/12/2222',
            en_time='10:22 AM',
            repeat_frequency='0'
        ), follow_redirects=True)
        rv = self.app.post('/add', data=dict(
            id=2,
            title='Essay',
            description='Data types and login information',
            category='355',
            st_date='12/12/2222',
            st_time='10:22 AM',
            en_date='12/12/2222',
            en_time='10:22 AM',
            repeat_frequency='0'
        ), follow_redirects=True)

        # assert that the two new events are in the db
        assert b'Reading' in rv.data
        assert b'Essay' in rv.data

        # input a title
        rv = self.app.get('/search?search=Essay')

        # assert that only the entry titled Essay is included
        assert b'Essay' in rv.data
        assert b'Reading' not in rv.data

    def test_search_none(self):
        """Tests that search works if no matching search terms"""
        self.create_account('Tommy', 'Titan', 'ttitan@iwu.edu', 'admin', 'default')
        self.login('admin', 'default')
        # add an event

        rv = self.app.post('/add', data=dict(
            id=1,
            title='Reading',
            description='Data types and login information',
            category='355',
            st_date='12/12/2222',
            st_time='10:22 AM',
            en_date='12/12/2222',
            en_time='10:22 AM',
            repeat_frequency='0'
        ), follow_redirects=True)
        rv = self.app.post('/add', data=dict(
            id=2,
            title='Essay',
            description='Data types and login information',
            category='355',
            st_date='12/12/2222',
            st_time='10:22 AM',
            en_date='12/12/2222',
            en_time='10:22 AM',
            repeat_frequency='0'
        ), follow_redirects=True)

        # assert that the two new events are in the db
        assert b'Reading' in rv.data
        assert b'Essay' in rv.data

        # input a title
        rv = self.app.get('/search?search=Wumbo')

        # assert that no entries are shown
        assert b'Reading' not in rv.data
        assert b'Essay' not in rv.data
        assert b'No results' in rv.data

        rv = self.app.get('/')

        # assert that the entries are still on the main page
        assert b'Reading' in rv.data
        assert b'Essay' in rv.data
        assert b'No tasks so far' not in rv.data

    def test_reminder(self):
        # unit tests for checking if reminders are displayed

        # create and login to account
        self.create_account('Tommy', 'Titan', 'ttitan@iwu.edu', 'admin', 'default')
        self.login('admin', 'default')

        # get today's date
        current_time = datetime.datetime.now()
        today_date = current_time.strftime('%m/%d/%Y')

        # add an event
        rv = self.app.post('/add', data=dict(
            id=1,
            title='Reading',
            description='Data types and login information',
            category='355',
            st_date='11/25/2222',
            st_time='10:22 AM',
            en_date=today_date,
            en_time='10:22 AM',
            repeat_frequency='0'
        ), follow_redirects=True)

        # assert reminder is in db
        assert b'Today: Reading' in rv.data

""" This unit test needs to be updated now that check/uncheck do not flash alerts
    def test_check_messages(self):
        self.create_account('Tommy', 'Titan', 'ttitan@iwu.edu', 'admin', 'default')
        self.login('admin', 'default')

        rv = self.app.post('/add', data=dict(
            id=1,
            title='Reading',
            description='Data types and login information',
            category='355',
            st_date='12/22/2222',
            st_time='12:22 AM',
            en_date='02/28/2222',
            en_time='12:22 AM',
            repeat_frequency='0'
            ), follow_redirects=True)

        assert b'Reading' in rv.data
        assert b'No tasks so far' not in rv.data

        # check off entry for id = 1
        rv = self.app.post('/check_entry', data=dict(
            id=1
        ), follow_redirects=True)

        # assert the event was checked off successfully
        assert b'Event Checked! Good work' in rv.data
        assert b'Event Unchecked! Get back to work!' not in rv.data

        # uncheck the entry for id = 1
        rv = self.app.post('/uncheck_entry', data=dict(
            id=1
        ), follow_redirects=True)

        # assert the event was unchecked successfully
        assert b'Event Unchecked! Get back to work!' in rv.data
        assert b'Event Checked! Good work' not in rv.data
"""
if __name__ == '__main__':
    unittest.main()
