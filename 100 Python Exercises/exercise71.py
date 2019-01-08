#Question:
'''
Count the number of "a" characters in this text file:
http://www.pythonhow.com/data/universe.txt

Hint: Use the requests  library to load the text file content in Python and
then use the count  method.
'''
#Answer:
'''
import requests

response = requests.get("http://www.pythonhow.com/data/universe.txt")
text = response.text
count_a = text.count("a")
print(count_a)

Explanation:

This is like the previous exercise. We're simply applying the count  method
here to the loaded string.
'''
