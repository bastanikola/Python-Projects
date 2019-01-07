-------------------------------------
### PROJECT: LAW OF LARGE NUMBERS ###
-------------------------------------
'''
Test the law of large numbers for N random normally
distributed numbers with mean = 0, stdev = 1:

Create a Python script that will count how many of
these numbers fall between -1 and 1 and divide
by the total quantity of N

You know that E(X) = 68.2%

Check that Mean(Xn) converge to E(X) as you rerun
the script while increasing N
'''

import numpy as np
from numpy.random import randn

N = 1000
counter = 0

for i in randn(N):
    if i > -1 and i < 1:
      counter = counter +1

counter/N
