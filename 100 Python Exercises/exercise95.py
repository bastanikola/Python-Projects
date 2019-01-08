#Question:
'''
Create a program that ask the user to input values separated by commas and
those values will be stores in a separated line each in a text file

Hint: Think of splitting the user string.
'''
#Answer:
'''
line = input("Enter values: ")
line_list = line.split(",")
with open("user_data_commas.txt, a+") as file:
    for i in line_list:
        file.write(i + "\n")

Explanation:

In line 1 we ask the user to input the values and in line 2 we create a list
containing the user submitted values. Then, in line 3 we open a file in a+  mode
(read and append). If there's no file with such name, it will be created. Then
in line 4 and 5 we iterate through the list and write those lines in the opened
file.
'''
