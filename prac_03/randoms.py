import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
What did you see on line 1?
*A random integer between 5 and 20.

What was the smallest number you could have seen, what was the largest?
*5 and 20

What did you see on line 2?
*A random numbers from 3 to 10 in steps of 2.

What was the smallest number you could have seen, what was the largest?
*3 and 9

Could line 2 have produced a 4?
*No

What did you see on line 3?
*A random floating number between 2.5 and 5.5

What was the smallest number you could have seen, what was the largest?
*2.5 and 5.5
"""
#Write code, not a comment, to produce a random number between 1 and 100 inclusive
random_number = random.randint(1, 100)
print(random_number)