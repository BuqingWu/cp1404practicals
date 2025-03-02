"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
code_to_name = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(code_to_name)

state_code = input("Enter short state: ")
while state_code != "":
    state_code = state_code.upper()
    if state_code in code_to_name:
        print(f"{state_code} is {code_to_name[state_code]}")
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")

print("\nAll states and names:")
for code, name in code_to_name.items():
    print(f"{code:3} is {name}")