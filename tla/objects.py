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
    def __init__(self, task_name = "FooTask", members_needed = 0, members_list = []):
        self.name = task_name
        self.needed = members_needed
        self.members = members_list
    
    #str method
    def __str__(self):
        return f"Task Name: {self.name}\n"
    
    #accessor mehods
    def get_name(self):
        return self.name
    
    def get_needed(self):
        return self.needed
    
    def get_members(self):
        return self.members
    
    #mutator method
    def add_members(self, member):
        self.members.append(member)

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
    
    #Member Methods
    
    def assign_members(self):
        from random import shuffle
        unassigned_members = self.get_members()
        shuffle(unassigned_members)
        
        #have to check why it is that all tasks passed through this method have 2 members assigned
        
        for task in self.tasks:
            needed = task.get_needed()
            while len(task.get_members()) < needed:
                task.add_members(unassigned_members.pop())