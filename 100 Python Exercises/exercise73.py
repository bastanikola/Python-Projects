#Question:
'''
Multiply the values of the text files in the URL by two and export the output
to a new file

Hint: The easiest way to do this is with pandas.
'''
#Answer:
'''
import pandas

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data_2 = data * 2
data_2.to_csv("sampledata_x_2.txt", index=None)

Explanation:

As you can see this can be done with pandas in four lines of code. We use
read_csv  to create a pandas dataframe object which is like a table with data.
Then we multiply this table by two and then export the calculated data to a
text file in our local directory.
'''
