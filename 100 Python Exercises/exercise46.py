#Question:
'''
Write a script that extract letters from the 26 text files and put the letters
in a list.

Hint: Use glob.glob to create a list of file paths and then iterate through
that list reading the content of each file.
'''
#Answer
'''
import glob

letters = []

file_list = glob.glob("letters/*.txt")

for filename in file_list:
    with open(filename, "r") as file:
        letters.append(file.read().strip("\n"))

print(letters)
'''
