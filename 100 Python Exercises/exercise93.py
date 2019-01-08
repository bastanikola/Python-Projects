#Question:
'''
Please download the attached ZIP file. Inside the ZIP file there's a directory
named subdirs. That directory contains other directories inside. Please write a
script that counts the number of .py files contained inside subdirs and all its
sub-directories.

Hint: You could use glob.glob  here with recursive set to True
'''
#Answer:
'''
import glob

file_list = glob.glob("subdirs/**/*.py", recursive=True)
print(len(file_list))

Explanation:

We're using glob.glob  in contrast to glob.glob1, gets a pathname pattern and a
recursive  argument which indicates whether you want to search sub-directories
or not.
'''
