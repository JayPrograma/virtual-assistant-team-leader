# Team Leader Assistant

## Introduction:
The following piece of software is a simple program designed to serve as a virtual assistant to a Team Leader in a service program.
Uses for the TLA include delegating tasks to members in a random and fair manner, keeping track of who they've worked with,
and keeping track of what tasks they've done before.

## TODO:
*   Modify assign_members() method in Project class to account for cases of there being less members than there are tasks and vice-versa
*   Create some kind of text-based CLI
*   Look into moving the __str__ method duties from the Member, Task, and Project classes to the CLI file if optimal, else keep the same
*   Create functionality to save and load information from external file

## Changelog:

### 12/30/24:
*   Modified Task __str__ method to provide more information
*   Encountered the Mutable Default Argument in Python... Most Astonishment, and changed the way I established the default list arugments for the Task and Project classes :)

### 12/29/24:
*   Removed Tests folder and simply placed the tests_basic.py file on highest-level directory in package /tla/
*   Removed certain methods in Project and Task classes that were unnecessary right now
*   Renamed "participants" to "members" in Task class for consistency with other class naming conventions
*   Redid test folder to test the methods in the Member, Task, and Project classes

### 12/27/24: 
*   Updated README to have a different format
*   Added a Todo list with items for follow-up.
*   Added an add_task method to project class.
*   Added a simple documentation line on tests_basic
*   Added Accessor Methods for the Member, Task, and Project classes
*   Changed folder name for sample to tla, with main.py now being tla.py
*   Added concepts of a unit test for adding members to a task, still unfinished