"""
    Members

    This is a module containing the Member, Task and Project classes.
"""


class Member:
    # defining init method with parameters
    def __init__(self, first="Foo", last="Bar"):
        self.first_name = first
        self.last_name = last

    # str method
    def __str__(self):
        return f"Member: {self.last_name}, {self.first_name} \n"

    # defining accessor methods
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name


class Task:
    # init method
    def __init__(self, task_name="FooTask", members_needed=0, members_list=None):
        self.name = task_name
        self.needed = members_needed

        if members_list is None:
            self.members = []
        else:
            self.members = members_list

    # str method
    def __str__(self):
        message = f"Task Name: {self.name}\n"
        message += f"Members Needed: {self.needed}\n"
        message += "Members:\n"
        for member in self.members:
            message += str(member)
        message += "-------------------------------------------------\n"

        return message

    #accessor mehods
    def get_name(self):
        return self.name

    def get_needed(self):
        return self.needed

    def get_members(self):
        return self.members

    #mutator method
    def add_member(self, member):
        self.members.append(member)


class Project:
    # init method
    def __init__(self, project_name="FooProject", members_list=None, task_list=None):
        self.name = project_name

        if members_list is None:
            self.members = []
        else:
            self.members = members_list

        if task_list is None:
            self.tasks = []
        else:
            self.tasks = task_list

    # str method
    def __str__(self):
        return f"Project Name: {self.name}\n"

    # Accessor methods
    def get_name(self):
        return self.name

    def get_members(self):
        return self.members

    def get_tasks(self):
        return self.tasks

    # constructor methods
    def add_task(self, task_name = "FooTask", members_needed = 0, members_list = None):
        self.tasks.append(Task(task_name, members_needed, members_list))

    # Member Methods
    
    def remove_task(self, task_name):  
        """
        Removes the task taken in as an argument from the list of tasks in the project class object
        
        Args:
            task_name (str): removes the str input from the task list in the project
        """
        for task in self.tasks:
            if task.get_name() == task_name:
                
                task_index = self.tasks.index(task)
                
                self.tasks.pop(task_index)

    def assign_members(self):
        from random import shuffle
        working_members = self.get_members()
        working_tasks = self.get_tasks()

        shuffle(working_members)
        shuffle(working_tasks)

        iterator1 = 0 # iterator that goes through member list

        for task in working_tasks:
            if iterator1 >= len(working_members):
                iterator1 = 0
            for i in range(task.get_needed()):
                task.add_member(working_members[iterator1])
                iterator1+=1