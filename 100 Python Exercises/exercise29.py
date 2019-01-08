#Question:
'''
Please write a function that calculates liquid volume in a sphere using the
following formula. The radius r  is always 10, so consider making it a
default parameter.

http://www.1728.org/spherprt.gif

You can then test your solution by passing 2 for h and you should get the
expected output.

Expected output:
4071.5040790523717

Hint: Your function should start with something like def volume(h, r = 10):
'''
#Answer
'''
from math import pi

def volume(h, r = 10):
    lv = ((4 * pi * r**3)/3) - (pi * h**2 * (3*r-h)/3)
    return lv
print(volume(2))
'''
