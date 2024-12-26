""" 
    Members
    
    This is a module containing the Member and Task classes.
"""

class Member:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        
    def __str__(self):
        return f"{self.last_name}, {self.first_name}: \n"

class Task:
    def __init__(self, task_name):
        self.name = task_name
        self.partner_list = []
        
    def populate_partners(self, cm_list):
        pass
        