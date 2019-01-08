#Question:
'''
Please download the attached ZIP file and extract its files in a folder.
Then, write a script that counts and prints out the number of .py files in
that folder.

Hint: An easy way to do this is to use glob.glob1 .
'''
#Answer:
'''
import glob

file_list=glob.glob1("files","*.py")
print(len(file_list))

Explanation:

We're using glob  which is a standard Python library that finds pathnames
matching a specified pattern. From glob  we're using glob1  which takes a
directory name as first argument and a pattern which in our case is *.py  which
returns all the files starting with whatever and ending with .py in the files
directory.
'''
