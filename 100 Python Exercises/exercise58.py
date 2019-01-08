#Question:
'''
Please download the json file in the attachment and use Python to add a new
employee to the content of the file.

Hint 1: Open the file in "r+" mode.

Hint 2: Create a dictionary out of the file content with json.loads, add the
new pair of key and value to the dictionary,  do file.seek(0)  to put the
cursor at the top of the file and then dump the dictionary to the opened file
again.
'''
#Answer
'''
with open("company1.json", "r+") as file:
    d = json.load(file.read())
    d["employees"].append(dict(firstName = "Albert", lastName = "Bert")
    file.seek(0)
    json.dump(d,file,indendt=4, sort_keys=True)
    file.truncate
'''
