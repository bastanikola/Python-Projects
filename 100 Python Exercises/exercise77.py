#Question:
'''
Create a script that asks the user to enter their age and the script calculates
the user's year of birth and prints it out in a string like in the expected
output. Please make sure you generate the current year dynamically.

Hint 1: Use input to prompt the user for their age.

Hint 2: To get the current year, use datetime.datetime.now().year .
'''
#Answer:
'''
from datetime import datetime

age = int(input("What's your age? "))
year_birth = datetime.now().year - age
print("We think you were born back in %s" % year_birth)

Explanation:

We're getting user input and we are converting it to an integer since input
loads everything as a string. Then we produce the current year dynamically with
datetime.now().year  and we subtract the age from that to find out the year of
birth. Lastly, in line 5, we use string formatting to produce a string with
the year inside it.
'''
