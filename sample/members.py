""" 
    Members
    
    This is a module containing the Member, Task and Project classes.
"""

class Member:
    def __init__(self, first = "Foo", last = "Bar"):
        self.first_name = first
        self.last_name = last
        
    def __str__(self):
        return f"Member: {self.last_name}, {self.first_name} \n"

class Task:
    def __init__(self, task_name = "FooTask", participant_list = []):
        self.name = task_name
        self.participants = participant_list
    
    def __str__(self):
        return f"Task Name: {self.name}\n"
    
    def add_participant(self):
        """
        Adds a Member to the task participants list.
        """
        
        print("Please enter participant information: \n")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        self.participants.append(Member(first_name,last_name))
        

class Project:
    def __init__(self,project_name = "FooProject",members_list = [], task_list = []):
        self.name = project_name
        self.members = members_list
        self.tasks = task_list
        
    def __str__(self):
        return f"Project Name: {self.name}\n"
        
    def add_task(self):
        """
        Adds a task to the Project.
        """
        task_name = input("Please Enter Task Name: ")
        self.tasks.append(Task(task_name))
        