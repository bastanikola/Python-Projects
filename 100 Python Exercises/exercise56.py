#Question:
'''
Store the dictionary in a json file.

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

Hint 1: This can be done through the json built-in module.

Hint 2: Use open  to create a file named something like company1.json
and use json.dump  to write the dictionary to the file.
'''
#Answer:
'''
import json

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

with open("company1.json", "w") as file:
    json.dump(d, file, indent=4)

Explanation:

As you can see we created the json file using the standard file
handling method, but then we used json.dump  which makes it easy
to write the dictionary content to the file. The argument indent=4
will create 4 white spaces to indent the different levels of the
dictionary items.
'''
