"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

menu = ["(H)ello", "(G)ood", "(Q)uit"]

name = ""
while name == "":
    name = input("Enter name: ")

choice = ""
while choice != "Q":
    print(menu)
    choice = input(">>> ").upper()
    if choice != "H" and choice != "G" and choice != "Q":
        print("Invalid choice")
    if choice == "H":
        print(f"Hello {name}")
    if choice == "G":
        print(f"Goodbye {name}")
    if choice == "Q":
        print("Finished.")
        
        