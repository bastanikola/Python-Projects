#Question:
'''
Create a program that ask the user to submit text repeatedly. The program saves
the changes when User submits SAVE, but doesn't close the program. Program
saves the changes and closes when user sumbits CLOSE.

Hint: Like the previous exercise, but here you need more conditional lines.
'''
#Answer:
'''
file = open("user_data_save_close", "a+")

while True:
    line = input("Write a value: ")
    if line == "SAVE":
        file.close()
        file = open("user_data_save_close", "a+")
    elif line == "CLOSE":
        file.close()
        break
    else:
        file.write(line + "\n")
'''
