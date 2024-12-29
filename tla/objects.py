""" 
    Members
    
    This is a module containing the Member, Task and Project classes.
"""

class Member:
    #defining init method with parameters
    def __init__(self, first = "Foo", last = "Bar"):
        self.first_name = first
        self.last_name = last
        
    #str method
    def __str__(self):
        return f"Member: {self.last_name}, {self.first_name} \n"
    
    #defining accessor methods
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name

class Task:
    #init method
    def __init__(self, task_name = "FooTask", participant_list = []):
        self.name = task_name
        self.participants = participant_list
    
    #str method
    def __str__(self):
        return f"Task Name: {self.name}\n"
    
    #accessor mehods
    def get_name(self):
        return self.name
    def get_participants(self):
        return self.participants
    
    #member methods
    def add_participant(self, first = "Foo", last = "Bar"):
        """
        Adds a Member to the task participants list.
        """
        if first == "Foo":
            print("Please enter participant information: \n")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            self.participants.append(Member(first_name,last_name))
        else:
            self.participants.append(Member(first,last))
        

class Project:
    #init method
    def __init__(self,project_name = "FooProject",members_list = [], task_list = []):
        self.name = project_name
        self.members = members_list
        self.tasks = task_list
        
    #str method
    def __str__(self):
        return f"Project Name: {self.name}\n"
    
    #Accessor methods
    def get_name(self):
        return self.name
    def get_members(self):
        return self.members
    def get_tasks(self):
        return self.tasks
        
    def add_task(self, task_name="Foo", participant_list = []):
        """
        Adds a task to the Project.
        """
        if task_name == "Foo":
            input_name = input("Please Enter Task Name: ")
            self.tasks.append(Task(input_name, participant_list))
        else:
            self.tasks.append(Task(task_name, participant_list))