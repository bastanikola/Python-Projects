#Question:
'''
The following code prints Hello, checks if 2 is greater than 1 and then reaks
the loop because 2 is actually greater than 1. Therefore Hi is not printed out.
Please repleace break with smth else so that Hello and Hi are printed out
repeatedly.

while True:
    print("Hello")
    if 2 > 1:
        break
    print("Hi")

Hint: Just pass it.
'''
#Answer:
'''
while True:
    print("Hello")
    if 2 > 1:
        pass
    print("Hi")
'''
