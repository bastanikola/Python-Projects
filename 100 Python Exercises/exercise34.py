#Question:
'''
The following script throws a NameError  in the last line saying that c  is
not defined. Please fix the function so that there is no error and the
last line is able to print out the value of c  (i.e. 1 ).

def foo():
    c = 1
    return c
foo()
print(c)

Hint 1: The reason of the error is that c  exists only
inside the function namespace. In other words, c  is a local variable.

Hint 2: Simply declare c  as a global variable inside the function.
'''
#Answer:
'''
def foo():
    global c
    c = 1
    return c
foo()
print(c)

Explanation:

Adding global c  fixes the code. That line makes available name c in the global
namespace. Therefore,  print is able to access variable c.
'''
