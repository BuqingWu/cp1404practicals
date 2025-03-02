"""
Estimate: 30 minutes
Actual: 88 minutes
"""
def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        correct_name = input(f"Is your name {name}? (Y/n): ").strip().lower()
        if correct_name != "" and correct_name != "y":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name_from_email(email):
    name_part = email.split('@')[0]
    name = ' '.join(name_part.split('.')).title()
    return name

main()