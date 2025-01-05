"""
This is a module containing the functions necessary for the interface to the vatl program.
"""
from blessed import Terminal

def run_program():
    """
   Function to run the vatl program's main interface
    """
    term = Terminal()
    is_on = True
    input_value = ""

    with term.fullscreen():  # sets a new window for the program
        while is_on:
            print(term.home + term.clear)  #ensures window is cleared
            print("Welcome to the Virtual Assistant Team Leader Program.")
            print("Please select one of the following commands:")
            print("[1]  View Projects")
            print("[2]  Quit Program")
            
            input_value = term.inkey()  # gets user input
            
            if(input_value=="1"):
                view_projects()
            if(input_value=="2"):
                is_on = False
                
def view_projects():
    """
    
    """