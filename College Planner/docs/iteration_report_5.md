# ITERATION REPORT 5 - Team Planner

## Responsibilities / Completion of Responsibilities
**Alec Pilon**
- Having events show according to logged-in user

**Anna Sheaffer**
- Complete search suggestions based on database contents
- Adjust add to-do to make it dynamic

**Khumoyun Abdulpattoev**
- Calendar view
- Event repeat
- Crossing off to-do's

**Mishwa Bhavsar**
- Landing page
- Documentation/code polishing

# What was completed
**Alec Pilon**
- Story completed; events are now linked to user ids

**Anna Sheaffer**
- Search suggestions working based on titles in db
- Adjustments to search suggestions based on how unit tests work
- To-do now uses a modal pop-up window (not fully dynamic)

**Khumoyun Abdulpattoev**
- Calendar view
- Event repeat
- Cross-off to-do

**Mishwa Bhavsar**
- Landing page
- Documentation for unit tests
- Fix indentations and minor template errors
- Dropdown for reminders
- Added unit test for testing reminder feature

# What was planned but not finished
**Alec Pilon**
- Everything was completed

**Anna Sheaffer**
- To-do is not completely dynamic
- Current to-do format indicates that multiple events can be checked off at once but this is not possible

**Khumoyun Abdulpattoev**
- Everything was completed

**Mishwa Bhavsar**
- Everything was completed

# What troubles/issues/roadblocks/difficulties you encountered.
**Alec Pilon**
- I had difficulties figuring out how to attach the user_id of a user to the event when it was added, since nothing that identifies the user (like a username) is typed into the fields for the “add entry” form.

**Anna Sheaffer**
- I realized that any data from the database that is called from a query will be considered while running unit tests. Since I was gathering every title from the database for search suggestions to work, unit tests were no longer working properly because the data was still in rv.data even though it was shown in a different place.

**Khumoyun Abdulpattoev**
- Converting a date string to a datetime object can be confusing. Due to a date format change, I had to add some code that converts date string to a datetime object, add time delta to it, and convert back to a string 

**Mishwa Bhavsar**
- I think to figure out functionality of modal, collapse, and dropdown and deciding which one is the right fit was challenging. I wanted to add bell icon for reminders on navigation bar but importing Bootstrap’s icons is challenging as nothing was displaying. I will be working on this for next week and seeking out for help. 

# What adjustments to your overall design you discovered.
**Alec Pilon**
- I initially was going to try to use jinja templating (with if statements) to display the events according to the logged in user. It turns out I can do it all using back-end code in the .py file. 

**Anna Sheaffer**
-  With the way our unit tests are currently set up, from a programming standpoint it makes the most sense to only be able to search from the filtered posts. I am unsure whether this makes sense from a usability standpoint, though.
- Allowing multiple to-do's to be crossed off at once for checkbox-style to-do list would make sense from a usability standpoint.

**Khumoyun Abdulpattoev**
- Filter by category needs to be on the side of the calendar and show_events and filter_date need to be edited so only one remains

**Mishwa Bhavsar**
- Change reminder from collapse to dropdown

# One important thing you learned during this iteration.
**Alec Pilon**
- I learned that Flask’s session object acts like a dictionary and can be used to store a variety of things, not just a bool. This is really useful for storing small bits of information across the application without a full database or worse, a global variable. 

**Anna Sheaffer**
- While Javascript is a good tool for making webpages dynamic, there are many design and programming considerations that need to be made outside of just rendering HTML pages using data from the backend.

**Khumoyun Abdulpattoev**
- I have learned to use Python datetime and convert a date string to an object and vice versa

**Mishwa Bhavsar**
- I learned how to import images in PyCharm, different figures of Bootstrap, and html functionality 

# ITERATION PLAN

## User Stories Week 6
**Alec Pilon**
- Change event check to checkbox
- Make event check dynamic

**Anna Sheaffer**
- Allow multiple to-do items to be checked off in a single form
- Add multiple to-do's without the modal window closing

**Khumoyun Abdulpattoev**
- Have show_events reflect the dates that are chosen from the calendar rather than just listing all events in the database.
- Create a separate side div for filter by category
- Allow the user to not input a category and a blank does not appear in dropdown menu for filter

**Mishwa Bhavsar**
- Add icons for settings and reminders
- Add documentation for templates
- Looking for any bugs and fixing them
- Tutorial on landing page

Pull request reviewer: Mishwa