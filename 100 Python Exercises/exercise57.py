#Question:
'''
Please download the file in the attachment and use Python to print out its
content.

Hint: This can be done through the json  and the pprint built-in modules.
'''
#Answer:
'''
import json
from pprint import pprint

with open("company1.json","r") as file:
    d = json.loads(file.read())

pprint(d)

Explanation:

We're opening the file in read mode and then using json.loads which gets a
string as output and creates a dictionary object out of that.
'''
