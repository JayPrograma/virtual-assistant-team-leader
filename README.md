# Team Leader Assistant

## Introduction:
The following piece of software is a simple program designed to serve as a virtual assistant to a Team Leader in a service program.
Uses for the TLA include delegating tasks to members in a random and fair manner, keeping track of who they've worked with,
and keeping track of what tasks they've done before.

## TODO:
*   Modify tests_basic.py to adhere to PEP8 standards
*   Modify assign_members() method in Project class to account for cases of there being less members than there are tasks and vice-versa
*   Add the utility to remove tasks once complete. Have these be stored in an archived project
*   Create some kind of text-based interface
*   Create functionality to save and load information from external file

## Changelog:
### 01/05/24:
*   Created interface.py to hold all the functions that will be used in the user interface.
    *   Using Blessed to create a TUI
*   Added tests for new add_task and remove_task functions in Class project.
*   Created setup.py, which will hold all functions for the loading and saving of data for vatl use.

### 01/01/24:
*   Added a remove_task and add_task methods to the Project class.
*   Made changes to existing code in objects.py to better adhere to PEP8 standards.
*   Changed name of project to reflect common nomenclature in the target audience.
*   Changed structure of project directory to adhere to modern recommendations per the Python Packaging User Guide.

### 12/30/24:
*   Modified Task __str__ method to provide more information.
*   Encountered the Mutable Default Argument in Python... Most Astonishment, and changed the way I established the default list arugments for the Task and Project classes :)

### 12/29/24:
*   Removed Tests folder and simply placed the tests_basic.py file on highest-level directory in package /tla/.
*   Removed certain methods in Project and Task classes that were unnecessary right now.
*   Renamed "participants" to "members" in Task class for consistency with other class naming conventions.
*   Redid test folder to test the methods in the Member, Task, and Project classes.

### 12/27/24: 
*   Updated README to have a different format.
*   Added a Todo list with items for follow-up.
*   Added an add_task method to project class.
*   Added a simple documentation line on tests_basic.
*   Added Accessor Methods for the Member, Task, and Project classes.
*   Changed folder name for sample to tla, with main.py now being tla.py.
*   Added concepts of a unit test for adding members to a task, still unfinished.