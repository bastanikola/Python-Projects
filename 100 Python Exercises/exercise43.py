#Question:
'''
Create a script that generates a file where all letters of English alphabet are
listed two in each line. The inside of the text file would look like:

ab
cd
ef

and so on.

Hint 1: Use the zip  function to iterate through two slices of the letters
sequence.

Hint 2: One slice would be string.ascii_lowercase[0::2]  and the other
string.ascii_letters[1::2]
'''
#Answer
'''
import string

with open("words4.txt", "w") as file:
    for letter1, letter2 in zip(string.ascii_lowercase[0::2], string.ascii_lowercase[1::2]):
        file.write(letter1 + letter2 + "\n")
'''
