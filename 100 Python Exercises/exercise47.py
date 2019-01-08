#Quesiton:
'''
Write a script that iterates through each of 26 text files check if the letter
inside the text is in the string "python" and puts the letter in a list if the
letter is a character of "python".

Hint: Like the previous exercise, but here you need to add a conditional
inside the loop
'''
#Answer:
'''
import glob

letters = []
file_list = glob.iglob("letters/*.txt")
check = "python"

for filename in file_list:
    with open(filename,"r") as file:
        letter = file.read().strip("\n")
        if letter in check:
            letters.append(letter)

print(letters)

Explanation:

The glob module here helps to generate a list of text files. Then we iterate
through that list and read each file inside the loop, strip "\n" characters and
then check if the letter extracted from the file is in string "python" and we
append that letter if it is.
'''
