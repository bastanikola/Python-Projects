#Question:
'''
Add the missing items to the File

Hint: We have two lists. We just need to concatenate them and then sort the
concatenated list.
'''
#Answer:
'''
checklist = ["Portugal", "Germany", "Spain"]
checklist = [i + "\n" for i in checklist]

with open("country_missing.txt", "r") as file:
    content = file.readline()

update_list = sorted(checklist + content)

with open("country_missing_fixed.txt", "w") as file:
    for i in update_list:
        file.write(i)
'''
