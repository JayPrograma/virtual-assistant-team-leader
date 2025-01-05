"""
This file contains the unit tests for the Team Leader Assistant Project.
"""
from src.vatl import objects
import unittest as ut

class TestMemberClass(ut.TestCase):
    #test accessor methods
    
    def test_get_first_name(self):
        test_member = objects.Member("John", "Doe")
        self.assertEqual(test_member.get_first_name(), "John", "There's a issue with get_first_name!")
        
    def test_get_last_name(self):
        test_member = objects.Member("John", "Doe")
        self.assertEqual(test_member.get_last_name(), "Doe", "There's an issue with get_last_name!")

class TestTaskClass(ut.TestCase):
    #test accessor methods
    
    def test_get_name(self):
        john = objects.Member("John","Doe")
        fulano = objects.Member("Fulano", "de Tal")
        test_task = objects.Task("Shopping", 2, [john, fulano])
        self.assertEqual(test_task.get_name(),"Shopping", "There's an issue with get_name!")
    
    def test_get_needed(self):
        john = objects.Member("John","Doe")
        fulano = objects.Member("Fulano", "de Tal")
        test_task = objects.Task("Shopping", 2, [john, fulano])
        self.assertEqual(test_task.get_needed(), 2, "There's an issue with get_needed!")
        
    def test_get_members(self):
        john = objects.Member("John","Doe")
        fulano = objects.Member("Fulano", "de Tal")
        test_task = objects.Task("Shopping", 2, [john, fulano])
        expected_members = [john, fulano]
        self.assertEqual(test_task.get_members(), expected_members, "There was an error with get_members!")

class TestProjectClass(ut.TestCase):
    #test accessor methods
    def test_get_name(self):
        
        john = objects.Member("John","Doe")
        fulano = objects.Member("Fulano", "de Tal")
        test_member_list = [john, fulano]
    
        task1 = objects.Task("Shopping", 2, test_member_list)
        task2 = objects.Task("Demolition", 2, test_member_list)
        test_task_list = [task1, task2]
        
        test_project = objects.Project("Test", test_member_list, test_task_list)
        
        self.assertEqual(test_project.get_name(), "Test", "Something is wrong with get_name!")
        
    def test_get_members(self):
        
        john = objects.Member("John","Doe")
        fulano = objects.Member("Fulano", "de Tal")
        test_member_list = [john, fulano]
    
        task1 = objects.Task("Shopping", 2, test_member_list)
        task2 = objects.Task("Demolition", 2, test_member_list)
        test_task_list = [task1, task2]
        
        test_project = objects.Project("Test", test_member_list, test_task_list)
        
        self.assertEqual(test_project.get_members(), [john, fulano], "Something is worng with get_members!")
    
    def test_get_tasks(self):
        john = objects.Member("John","Doe")
        fulano = objects.Member("Fulano", "de Tal")
        test_member_list = [john, fulano]
    
        task1 = objects.Task("Shopping", 2, test_member_list)
        task2 = objects.Task("Demolition", 2, test_member_list)
        test_task_list = [task1, task2]
        
        test_project = objects.Project("Test", test_member_list, test_task_list)
        
        self.assertEqual(test_project.get_tasks(), [task1, task2], "Something is wrong with get_tasks!")
    
    #test constructor methods
    def test_add_task(self):
        member1 = objects.Member("John1", "Doe1")
        member2 = objects.Member("John2", "Doe2")
        member3 = objects.Member("John3", "Doe3")
        member4 = objects.Member("John4", "Doe4")
        member_list = [member1, member2, member3, member4]
        
        test_project = objects.Project("Project1", member_list)
        
        test_task = objects.Task("Task1", 2)
        
        test_project.add_task(test_task)
        task_list = test_project.get_tasks()
        
        self.assertEqual(task_list[0],test_task, "Error with add_task")

    #test member methods
    def test_assign_members(self):
        member1 = objects.Member("John1", "Doe1")
        member2 = objects.Member("John2", "Doe2")
        member3 = objects.Member("John3", "Doe3")
        member4 = objects.Member("John4", "Doe4")
        member_list = [member1, member2, member3, member4]
        
        task1 = objects.Task("Task1", 1)
        task2 = objects.Task("Task2", 1)
        task3 = objects.Task("Task3", 2)
        tasks_list = [task1, task2, task3]
        
        test_project = objects.Project("Project1", member_list, tasks_list)
        
        test_project.assign_members()
        
        assigned_tasks = test_project.get_tasks()
        
        self.assertEqual(len(assigned_tasks[0].get_members()), assigned_tasks[0].get_needed(), "Error in Task1")
        self.assertEqual(len(assigned_tasks[1].get_members()), assigned_tasks[1].get_needed(), "Error in Task2")
        self.assertEqual(len(assigned_tasks[2].get_members()), assigned_tasks[2].get_needed(), "Error in Task3")
        
    def test_remove_task(self):
        member1 = objects.Member("John1", "Doe1")
        member2 = objects.Member("John2", "Doe2")
        member3 = objects.Member("John3", "Doe3")
        member4 = objects.Member("John4", "Doe4")
        member_list = [member1, member2, member3, member4]
        
        task1 = objects.Task("Task1",2)
        task2 = objects.Task("Task2",2)
        task_list = [task1, task2]
        
        test_project = objects.Project("Project1", member_list, task_list)
        
        test_project.remove_task("Task1")
        
        self.assertEqual(len(test_project.get_tasks()), 1, "Error with remove_task!")


if __name__ == "__main__":
    ut.main()
