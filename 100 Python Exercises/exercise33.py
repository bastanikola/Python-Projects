#Question:
'''
Here's another similar exercise. What will the following script output?
Try to do this mentally if you can.

c = 1
def foo():
    c = 2
    return c
c = 3
print(foo())

Hint: Note that c  is a local variable that exists only inside the function.
The other two c  variables are global variables and have nothing to do with
the function
'''
#Answer:
'''
Python will print 2
'''
