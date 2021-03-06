#Question:
'''
Create a program that prints out Hello every two seconds.

Expected output:

...
Hello
Hello
Hello
Hello
Hello
Hello
...

Hint: Make the program sleep  for two seconds using he time  module.
'''
#Answer:
'''
import time

while True:
    print("Hello")
    time.sleep(2)

Explanation:

The sleep  method of the built-in time module suspends the execution of the
script for the given number of seconds.
'''
