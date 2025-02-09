"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)


def main():
    """A menu to help users solve the conversion between Fahrenheit and Celsius."""
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            convert_Celsius_to_Fahrenheit()
        elif choice == "F":
            convert_Fahrenheit_to_Celsius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def convert_Celsius_to_Fahrenheit():
    """Convert Celsius to Fahrenheit"""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")

def convert_Fahrenheit_to_Celsius():
    """Convert Fahrenheit to Celsius"""
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")

main()