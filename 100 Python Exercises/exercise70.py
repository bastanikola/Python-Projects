#Question:
'''
Print out the text of this file http://www.pythonhow.com/data/universe.txt.
Please don't manually download the file. Let Python do all the work.

Hint: Use the requests  library.
'''
#Answer:
'''
import requests
response = requests.get("http://www.pythonhow.com/data/universe.txt")
text = response.text
print(text)

Explanation:

We're using the get  method of the requests  library here which produces a
response  object in line 2. Then, in line 3 we apply the text property
to that response object to get the text of the loaded webpage.
'''
