# ITERATION REPORT 6 - Team Planner

## Responsibilities / Completion of Responsibilities
**Alec Pilon**
- Make event checking dynamic and also a checkbox

**Anna Sheaffer**
- Complete search suggestions based on database contents
- Adjust add to-do to make it dynamic

**Khumoyun Abdulpattoev**
- Have show_events reflect the dates that are chosen from the calendar rather than just listing all events in the database.
- Create a separate side div for filter by category
- Fix filter by category so a blank category (empty one) does not appear in dropdown menu for filter

**Mishwa Bhavsar**
- Add icons for settings and reminders
- Add documentation for templates
- Looking for any bugs and fixing them
- Tutorial on landing page

# What was completed
**Alec Pilon**
- Story completed 
- Fixed events for all users appearing for all users, made event check dynamic as well as changed its colors and placement

**Anna Sheaffer**
- Multiple to-do’s can be checked off prior to clicking ‘All Done!’ button
- The add to-do form and delete to-do form are in the same div.

**Khumoyun Abdulpattoev**
- Have show_events reflect the dates that are chosen from the calendar rather than just listing all events in the database.
- Create a separate side div for filter by category
- Fix filter by category so a blank category (empty one) does not appear in dropdown menu for filter

**Mishwa Bhavsar**
- Icons for Settings and Reminders

# What was planned but not finished
**Alec Pilon**
- Everything was completed

**Anna Sheaffer**
- Keeping the todo div open after adding an event to the form

**Khumoyun Abdulpattoev**
- Everything was completed

**Mishwa Bhavsar**
- Looking for any bugs and fixing them
- Tutorial on landing page
- Documentation for templates

# What troubles/issues/roadblocks/difficulties you encountered.
**Alec Pilon**
- Submitting by only clicking a checkbox turned out to be difficult to do because of the nature of checkboxes 
  designed to be used in conjunction with some sort of submit button.

**Anna Sheaffer**
- Keeping a div open after submitting a form is more complicated than I originally thought. Since div’s are not a 
  separate page with a separate template, you cannot reload the page in the same way you can with a page. 
  Any attempt at keeping the window open after submitting to a form with javascript does not automatically update the todo list with the new items. There are a lot of moving parts that make this more complicated than it may seem.

**Khumoyun Abdulpattoev**
- Submitting two forms on the same page messes up how we intend to show events. I am still figuring it out.

**Mishwa Bhavsar**
- Since we are still finalizing the styling and layout, I did not work on the tutorial. 
  I found a bug with padding within the navigation bar and I will be working on fixing it once every feature is 
  integrated and the display of events and calendar is finalized. People were still working on templates, 
  so we decided documentation would be done at a later stage.

# What adjustments to your overall design you discovered.
**Alec Pilon**
- Checkboxes are not well suited to what I was trying to do (a submit is required to update the database), so I decided to stick to a button

**Anna Sheaffer**
- It makes the most intuitive sense to have a single window for adding to-do’s and checking them off.

**Khumoyun Abdulpattoev**
- Showing searched events on a separate page 

**Mishwa Bhavsar**
- Using a icons instead of names under navigation bar

# One important thing you learned during this iteration.
**Alec Pilon**
- Extensive testing should be done with each pull request. Somehow my work last week was partially overwritten 
  last week, requiring the fix, due to issues we had from merging broken builds to main

**Anna Sheaffer**
- I have gained a better understanding of how forms work in relation to divs that can be turned on or off. Also, how 
  to handle multiple inputs into python.

**Khumoyun Abdulpattoev**
-  have gained better understanding of how requests work

**Mishwa Bhavsar**
-  I learned about changes in margin and padding 

# ITERATION PLAN

## User Stories for the next 2 weeks 
- Styling & Structure: 
  - Make the input fields required in html
  - Change styling for show events
  - Remove flash messages for dynamic features
  - Margin for navigation bar
- Validate email
- Reset password if forgotten
- Basic username/password constraints (no empty strings)
- Email validation on account creation
- Setting page: 
  - Page for Profile: Ability to change/update username, password, email address
- Dynamic delete event
- Functionality of reminder feature
- Redirect to another page for search results 
- Enable access to events for past dates 
- Documentation & Code Reviews
- Web Accessibility Check 
- Tutorial Page


## Who is responsible for them
**Alec Pilon**
- Basic username/password constraints (no empty strings)
- Documentation & Code Reviews
- Validate email

**Anna Sheaffer**
- Styling & Structure
- Redirect to another page for search results 

**Khumoyun Abdulpattoev**
- Enable access to events for past dates 
- Reset password if forgotten
- Web Accessibility Check 

**Mishwa Bhavsar**
- Dynamic delete event
- Functionality of reminder feature
- Settings page 
- Tutorial Page

Pull request reviewer: Khumoyun