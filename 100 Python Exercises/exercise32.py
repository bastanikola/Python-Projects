#Question:
'''
What will the following script output? Please try to do this mentally if
you can.

c = 1
def foo():
    return c
c = 3
print(foo())

Hint: At the time when the function is called c  has a value of 3.
'''
#Answer:
'''
Explanation:

Line 1: c  is assigned 1.
Line 2-3: We create a function which if executed will return the value of c .
Line 4: c  is updated and is now equal to 3.
Line 5: We tell the blueprint to print out the value of c  which is at the
point where we call the function 3.
'''
