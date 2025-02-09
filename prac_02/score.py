"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    check_score()

def check_score():
    """check user's score"""
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        if score > 90:
            print("Excellent")
        elif score < 50:
            print("Bad")
        else:
            print("Passable")

main()