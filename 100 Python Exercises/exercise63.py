#Question:
'''
Create a program that once executed the programs prints Hello instantly first,
then it prints it after 1 second, then after 2, 3, and then the program prints
out the message "End of the Loop" and stops.

Hint: Include an if  statement inside the loop and a break  statement inside
the conditional.
'''
#Answer:
'''
import time

i = 0
while True:
    print("Hello")
    i+=1
    if i > 3:
        print("End of the Loop")
        break
    time.sleep(i)
'''
