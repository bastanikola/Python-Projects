#Question:
'''
Why do you get an error and how would you fix it

def foo(a=2, b):
    return a + b

Hint: Always put non default parameters first followed by default ones.
'''
#Answer
'''
def foo(b, a=2):
    return a + b

Explanation

Non-default argument follows default argument
'''
