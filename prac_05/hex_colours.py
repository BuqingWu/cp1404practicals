COLOR_CODES = {
    "AliceBlue": "#f0f8ff", "Acid Green": "#b0bf1a", "Amethyst": "#9966cc", "Aquamarine1": "#7fffd4", "Aqua": "#00ffff",
    "Baby Blue": "#89cff0", "Baby Pink": "#f4c2c2", "Black": "#000000", "Chocolate": "#d2691e", "Blue": "#0000ff"}
print(COLOR_CODES)

color_name = input("Enter a color name (or press Enter to quit): ")
while color_name != "":
    color_name = color_name.strip().title()
    if color_name in COLOR_CODES:
        print(f"The hexadecimal code for {color_name} is {COLOR_CODES[color_name]}")
    else:
        print("Invalid color name. Please try again.")
    color_name = input("Enter a color name (or press Enter to quit): ")
print("Goodbye!")
