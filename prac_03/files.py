name = input("What is your name? ")
out_file = open("name.txt", 'w')
out_file.write(name)
out_file.close()

in_file = open("name.txt", 'r')
name_from_file = in_file.read().strip()
in_file.close()

print(f"Hi {name_from_file}!")

with open("numbers.txt", 'r') as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())

total = number1 + number2
print(total)

with open("numbers.txt", 'r') as in_file:
    total = 0
    for line in in_file:
        total += int(line.strip())

print(total)