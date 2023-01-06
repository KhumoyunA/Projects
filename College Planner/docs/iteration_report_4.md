# ITERATION REPORT 4 - Team Planner

We will work on templating once we have our calendar template is added, so we don’t have to restart templating again
What each person was responsible for accomplishing.

## Responsibilities / Completion of Responsibilities

**Alec Pilon**
 - Login and Logout 

**Anna Sheaffer**
- Event search, styling

**Khumoyun Abdulpattoev**
- Calendar view, event repeat, cross off  to-do

**Mishwa Bhavsar** 
- I was responsible for creating event reminders feature 

# What was completed.

**Alec Pilon**
- Added ability to create an account, login to an account and logout of active account

**Anna Sheaffer**
- Event search, some navbar styling, datepicker, timepicker

**Khumoyun Abdulpattoev**
- Calendar view 

**Mishwa Bhavsar** 
- Completed creating the event reminders
# What was planned but not finished.
**Alec Pilon**
- Everything was completed

**Anna Sheaffer**
- Search suggestions for event search

**Khumoyun Abdulpattoev**
- Event repeat, Cross off a to-do

**Mishwa Bhavsar**
- Everything was completed

# What troubles/issues/roadblocks/difficulties you encountered.
**Alec Pilon:** 
- I had to go to office hours for some strange sql/python stuff that led to me needing to understand how cur.fetchone works. 

**Anna Sheaffer:**
- Having data from the backend become usable in javascript on the frontend

**Khumoyun Abdulpattoev**
- Correctly connecting CSS and JS to the calendar was trickier than I expected 

**Mishwa Bhavsar**
- Currently, we are trying to figure out the calendar view and how we will store the date in the schema by using a date picker. So, the formatting for reminders will change. Also, the unit test for reminders was not written since the title of the event is already included on the main page, and the function get_reminder() is only displaying the title of events that are due on the main_page as well. 

# What adjustments to your overall design you discovered.

**Alec Pilon**
- Changing the login/logout button can be done via jinja templating

**Anna Sheaffer**
- Changing the database schema to be MM-DD-YYYY so that it is compatible with the jQuery datepicker. Also, adjusting add daily to-do so that it is dynamic and the page doesn’t render everytime something is added.

**Khumoyun Abdulpattoev**
- Changing schema. For now, we decided to have events that start/end within the same day as otherwise it would be harder to deal with events that last two or more days

**Mishwa Bhavsar**
- None

# One important thing you learned during this iteration.

**Alec Pilon**
- Jinja can do even more than I thought, it is able to get flask’s session object to see its status.

**Anna Sheaffer**
- Javascript can add a lot of additional functionality to a webpage, and we should consider using it for the rest of the project. 

**Khumoyun Abdulpattoev**
- Importing a calendar to the project is not as simple as it seems to be. Flask does not recognize templates outside of the templates folder, so files need to be moved around. I have learned to work with JS more since I had to integrate the calendar correctly

**Mishwa Bhavsar**
- Fixing merge conflicts during in-person meeting and helping each other out with explaining how other features work was helpful. I personally learned about the functionality of date-picker and login and log out. 


# ITERATION PLAN

# User Stories Week 5

**Alec Pilon**
- Displaying posts according to the logged in user

**Anna Sheaffer**
- Finish search bar suggestions so that it reflects data in the database, implement add daily to-do dynamically

**Khumoyun Abdulpattoev**
- Unknown

**Mishwa Bhavsar**
- Landing Page, documentation, code polish

Dependencies: None

Pull Request Reviewer: Anna