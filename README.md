# DjangoHR
## Overview
DjangoHR is a web application for the purpose of managing human resource affairs within an organization with the user being all employees within said organization. The application was done as a final project the course CS50 2020 - Web Programming with Python and Javascript.

This application was developed using the Django framework within Python 3.7 and Javascript with Bootstrap for front-end components providing responsive design. Django built in modules SQLite and tomcat were used for database and server instance.

## Project Description
This project meets all the requirements outlined in the final project requirements of the CS50 course.

Firstly, this application is not similar in any way to, is more complex than, and has more functionality than any applications developed in previous assignments as part of this course. The number of models (see below for a list of models) and the relationships between them meet the complexity requirements.

This application servers a very different purpose compared to the social network or the ecommerce assignments. This project allows management of multiple models and serves as a platform for an organization to track and manage human resource affairs and employee development.

The application uses multiple views for server-side data management in python and Javascript for front-end user interactions and updates with multiple templates to present information in the relevant context and checking permissions to facilitate different user roles.

## Installation
Download Git Repository
Python 3.7
Django

    python manage.py runserver

## Functions
**User Management**
The application requires login credentials for each user. Due to this application being planned to be extended to allow multiple organizations, an user cannot simply create an account using any email -they must use an email that is in the system. The account creation is controlled though an employee in the Human Resources Department who has more privileges than all other employees outlined below. A user must be created in the application by the HR employee and the email used must be provided to the new user for them to be able to register/create account in the  application.

Employee details of the logged in user can be viewed in the **Profile** tab. The **People** tab shows a list of all employees within the organization with a link to their profile which would show limited information. An HR Employee can edit the employee details when viewing their profile as outlined in the permissions section below. See the User model for more details on the associated employee object.

**Time Off Requests**
An employee can request a time in the **Time Off** tab and clicking "Request Time Off". They will be able to select the leave type (Vacation, Sick, Unpaid), the dates/duration of the leave and a comment. Validations are in place to prevent users from selecting invalid date range or requesting more days than they have available (for Vacation and Sick leaves only). The request will be sent to an HR employee for review.

The employee will also see a grid listing all of their requests from the past along with their details including the status.

**Leave Request Approval**
Only available to HR employees is a **Leave Requests** tab. This tab lists all the outstanding leave requests from employees awaiting approval providing details (days, dates, employee name, comment) about the request. The HR employee has the ability to Approve or Reject the request and add a comment of their own. 

All historical leave requests can also be viewed in a grid by clicked "Request History". It displays the leave type, dates/duration and the request status for reference in the future or audit purposes.

**Objectives**
This application also provides the functionality for all employees to be able to create objectives and follow up on them to track progress. This can be a useful tool to set goals and encourage self improvement. Employees can create objectives by providing a description and a due date. They can then "check in" to these objectives at later dates to update progress and finally close them out. Similarly to leave requests, they can view a history of their objectives with a couple different views for all objectives and a single objective and its check ins.

**Announcements**
On the landing page of the application, the employees will see any announcements that have been posted by HR (only HR employees have the ability to post an announcement). This could be useful to let all employees of any changes in the organization and welcome new employees.

## Models
Field details for each model can be viewed in the Django Admin application.

**Employee** - Associated to a single User in the application. Contains details about the employee's job position, education, name and address.
**LeaveRequest** - Model to house leave requests made by employees. Contains details such as dates, leave type and status.
**Announcement** - Model for announcements on the home page.
**Department** - Controlled vocabulary referenced by the Employee model for employee's job details. Contains reference to a Department Head.
**Position** -  Controlled vocabulary referenced by the Employee model for employee's job details. 
**Objective** - Model to house objectives created by employees. Contains details such as description, progress, due date, etc.
**CheckIn** - Object to track updates and relates to the Objective model.

## Application Files
**layout.html** - The base layout of the application page containing the header and references to bootstrap.
**login.html** - Page containing the login form.
**register.html** - Page containing the registration form.
**index.html** - The home page after logging in. Contains code for displaying announcements and the form to create a new announcement.
**profile.html** - Contains logic for displaying employee details of a given employee - used in **Profile** and **People** tab. Calls EmployeeForm to edit employeedetails.
**people.html** - Displays list of all employees. Uses profile.html to view details of a single employee.
**addEmployee.html** - Calls EmployeeForm to create/edit an employee.
**leaveRequests.html** - contains list of active requests to be reviewed and list of historical requests. Javascript listeners for data updates on Approve or Reject using fetch api.
**timeOff.html** - Shows list of all requests of a given employee. and the form to submit a new requests. Javascript data validations for invalid dates and accrued days for a given employee.
**objectives.html** -  Contains list of active and completed objectives with links for each objective and creating a new objective (references addObjective.html and viewObjective.html). Uses Javascript for form submissions.
**addObjective.html** - Modal form to add a new objective.
**viewObjective.html** - Objective "profile" displaying details and related check ins.
**checkIn.html** - Form to check in to an objective.
**styles.css** - global styles for all pages.
**admin.py** - registration of application models to the Admin application.
**forms.py** - Django form for Employee model.
**models.py** - All model definitions used in the application.
**urls.py** - endpoints and reference to views of the application.
**views.py** - contains most of the back-end code/logic for data processing and passing data into django templates for all endpoints. 
