"""A score menu"""
import random

MENU = "1.Get valid name, 2.print a line(of asterisks), 3.print random number, quit"

def main():
    """Get users choice"""
    choice = input("Enter your choice in menu(1/2/3/quit)")
    while choice != "quit":
        if choice == "1":
            name = get_valid_name()
        elif choice == "2":
            print_line_of_asterisks()
        elif choice == "3":
            print(random.randint)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Enter your choice in menu(1/2/3/quit)")

def get_valid_name():
    """Prompt the user to enter a name and return a valid name after verification."""
    name = input("Enter your name: ")
    if name == " ":
        name = input("Enter your name: ")

def print_line_of_asterisks():
    """Print a line of asterisks."""
    print("*" * 15)

main()
