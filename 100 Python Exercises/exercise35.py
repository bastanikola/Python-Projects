#Question:
'''
Create a function that takes any string as input and returns the number of
words for that string.

Hint 1: Convert the string to a list with split.


Hint 2: Once you do string.split(" "), then apply the len method to the
produced list.
'''
#Answer:
'''
def count_words(strng):
    strng_list = strng.split()
    return len(strng_list)

print(count_words("Hey there it's me!"))

Explanation:

We're using split  here which is a string method that splits a string into
several strings given a separator passed inside the brackets. When you don't
pass a separator, split  will split a string at white  spaces. This will output
a list of strings. Applying len  to that list returns the number of list items,
so the number of words.
'''
