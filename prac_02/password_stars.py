"""Module docstring"""

# imports
# CONSTANTS

def main():
    """Function docstring"""
    # statements...
    do_stuff()


def do_stuff():
    """Function docstring"""
    # statements...


main()

PASSWORD_LENGTH = 10

password = input("Enter password: ")
while len(password) < PASSWORD_LENGTH:
    print("Invalid Password")
    password = input("Enter password")

print(len(password) * "*")