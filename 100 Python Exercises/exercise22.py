#Question
'''
Create a dic of a, b, c, where each value a list 1 to 10, 11 to 20, 21 to 30
respectively and print out a resultself.

Hint: Use a range function to create the lists
'''
#Answer
'''
from pprint import pprint
my_dict = {"a" : list(range(1,11)), "b" : list(range(11,21)),
           "c" : list(range(21,31))}
pprint(my_dict)

Explanation:

We're using ranges here to construct the lists. We're also using the built-in
Python pprint  module which is used to print out well formatted views of
datatypes in Python.
'''
