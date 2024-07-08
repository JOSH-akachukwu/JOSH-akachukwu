"""This is a programe to which will teach a user some basics in python programming language"""
"""The main prpose for writing this code is to help me teach ebube."""

print("   Welcome to Python Tutorial     ")
print(" \n The python tutorial is an interactive learning environment where you can \n learn about the python programming language in a productive way. " )
print("enjoy the ride!!")
print('')

print("Table of contents")
print("1- Intro")
print("2- The print statement")
print("3- The input statement")
print("4- Variables")
print("5- Using varibles")
print("6- first closure.")

Intro = (
   '\n' "Welcome to introductory phase of this tutorial.Here you will get a brief walkthrough on this Tutorial"
    '\n'"First we will walk you through print function in python "
    '\n'"next you will proceed to the input function in python"
    '\n'"followed by an intro to variables, it meaning, uses and types"
    '\n'"further more you'll be taking a quick glance on how to use variables"
    '\n'"befor coming to the end of this tutorial"
)
Print_statement = (
    
    """
* The print statement
    The print statement tells the computer to display information on the monitor screen
    the print call has a very easy way of using it
    >>> print() <<<
    An example is;
        print("hello world")
    is the simple way to use the print statement
    give it a try."""
)
input_statement = (
    """
* The input statement
    It tells the computer to accept data from the user,afterwards uses it as programed
    the simple syntax for using the input statement is:
    >>> input() <<<
    An example is;
        input("Enter your name:")
    Give it a try."""
)

def input_state():
    x = input_statement
    print(x)
    return'' 
def print_state():
    x = Print_statement
    print(x)
    next = input("press enter to go to the next tutorial!")
    if next == '':
        print(input_state())
        return''


def intr():
    x =  Intro
    print(x)
    next = input("press enter to go to the next tutorial!")
    if next == '':
        print(print_state())
        return "DONE!!"

Ui = input("press enter to start, or, refer to any tutorial number to go directly to it.")
var = ''
if Ui == var:
    print(intr())
elif Ui == '2':
    print(print_state())
elif Ui == '3':
    print(input_state())
else:
    print("invalid input!")




