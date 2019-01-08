#Question:
'''
Please download the attached countries-raw.txt file. The file contains the list
of country names, but it also contains some unnecessary text among the
countries.

Please clean the list with Python by generating a new text file that contains a
flawless list of country names without any other text or break lines in it.
The new file content should look like in the expected output.

Hint: Load the existing file content to a list and then use list comprehensions
with if statements inside to iterate through the list items and check the items
if they are equal to things like "Top of Page", "\n" and so on.
'''
#Answer:
'''
with open("countries_raw.txt", "r") as file:
    content = file.readline()

#removing \n from our list and building a new list
content = [i.strip("\n") for i in content if "\n" in i]

#removing all empty strings and updating list
content = [i for i in content if i !='']

#removing string "Top of the page"
content = [i for i in content if i !="Top of the page"]

#removing strings if the len is = 1
content = [i for i in content if len(i) != 1]

print(content)

#writing a list into file
with open("countries_raw.txt", "w") as file:
    for i in content:
        file.write(i+"\n")
'''
