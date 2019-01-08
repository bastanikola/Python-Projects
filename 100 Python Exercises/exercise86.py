#Question:
'''
Please take a look at the following list:

#hecklist = ["Portugal", "Germany", "Munster", "Spain"]

One of the items is not a country. Please use Python and the file containing
the list of countries (attached) as data source to filter out the checklist
of non-country items. Once you have filtered out checklist , then print
it out.

Hint: Use list comprehensions and an if statement inside them.
'''
#Answer:
'''
checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open("countries-clean.txt", "r") as file:
    content = file.readlines()

content = [i.rstrip('\n') for i in content]
checked = [i for i in content if i in checklist]

print(checked)

Explanation:

We're opening our file data source and loading it in Python as a list in
content. Then we clean out that list of break lines in line 6. Then, in line 7
we check if the items of content  are in checklist , and if they are we leave
them in the list, otherwise, we remove them. So, we end up with only the three
matches.
'''
