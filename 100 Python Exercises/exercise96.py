#Question:
'''
Create a program taht ask the user to submit text repeatedly. The program
closes when the user submits CLOSE.

Hint: Consider using break in the while loop.
'''
#Answer:
'''
file = open("user_data.txt","a+")

while True:
    line = input("Write a value: ")
    if == "CLOSE":
        file.close()
        break
    else:
        file.write(line + "\n")
'''
