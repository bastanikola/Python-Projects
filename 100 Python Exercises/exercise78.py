#Question:
'''
Create a program that generates a password of 6 random alphanumeri charachters
in the range abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQR
STUVWXYZ!@#$%^&*()?

Hint: Use random.sample.
'''
#Answer:
'''
import random

characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
chosen = random.sample(characters, 6)
password = "".join(chosen)
print(password)

Explanation:

We're importing the random  module and using its sample method which picks 6
random items from the characters sequence. The items are stored in list chosen.
Then we use a string join  method to join the list items to a string.
'''
