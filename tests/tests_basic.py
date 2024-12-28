"""
This file contains the unit tests for the Team Leader Assistant Project.
"""
import tla.members as members # fix this!
import unittest as ut

class TestAddingParticipantToTaskAsParameter(ut.TestCase):
    def test(self):
        test_task = members.Task("Test1")
        control_member = members.Member("John", "Doe")
        test_task.add_participant("John","Doe")
        self.assertEqual(test_task.participants[0],control_member,"These are not the same")

#class TestAddingTaskToProject(ut.TestCase):
#    def test(self):
#        test_project = members.Project(Test1)
#        test_project.add_task()
#        sample_project = members.Project(Test2)
#        sample_project.add_task("Task1")
#        #compares the names of the two tasks for equivalency


if __name__ == "__main__":
    ut.main()