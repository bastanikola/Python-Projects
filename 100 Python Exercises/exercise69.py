#Question:
'''
Please create an empty file (manually as you normally create Python files) and
name it "requests.py". Make sure the file has that name exactly.

Then just paste the following code in the file:

import requests

r = requests.get("http://www.pythonhow.com")
print(r.text[:100])

Executing the script will throw an error. Please fix something to make the
program print out the expected output. You should not modify the code itself,
but something else.

Hint 1: The code generates an error that suggests the requests module does not
have a get  method. The requests library does actually have a get  method.

Hint 2: Import statements first look for a local file in the current directory
(e.g. requests.py). If there is such file it imports that file, and not the
actual module.
'''
#Answer:
'''
Rename the file name from requests.py  to something else.

Explanation:

In the code Python is actually referring to the script name which is requests
and it doesn't find a get attribute for that name. Script names load in the
current namespace. They are actually stored in the __name__  variable. You
could try to print that variable out and you would see that it prints your
script name. Therefore you should not name your scripts under library names.
'''
