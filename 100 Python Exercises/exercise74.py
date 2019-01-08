#Question:
'''
Please concatenate this file with this one to a single text file. The content
of the output file should look like below.

Expected output:
x,y
3,5
4,9
6,10
7,11
8,12
6,10
8,18
12,20
14,22
16,24

Hint 1: Use pandas  to open the two files as dataframes and the concat method
to concatenate the dataframes.

Hint 2: Once you have loaded the files with pandas.read_csv  and concatenated
with concat, use the to_csv  method with index=None  to export to a new file.
'''
#Answer 1:
'''
import pandas

data1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2 = pandas.read_csv("sampledata_x_2.txt")
data12 = pandas.concat([data1, data2])
data12.to_csv("sampledata12.txt", index=None)

Explanation 1:

Again we are using pandas to load the data into Python. Then in line 5, we use
the concat  method. The method expects as input a list of dataframe objects to
be concatenated. Lastly, in line 6, we export the data to a new text file.
'''
#Answer 2:
'''
import io
import pandas
import requests

r = requests.get("http://www.pythonhow.com/data/sampledata.txt")
c = r.content
data1 = pandas.read_csv(io.StringIO(c.decode('utf-8')))
data2 = pandas.read_csv("sampledata_x_2.txt")
data12 = pandas.concat([data1, data2])
data12.to_csv("sampledata12.txt", index=None)

Explanation 2:

In answer 1 we passed the file url directly into read_csv . The read_csv
method uses the urllib library internally to download the file. In case of
errors with urllib you can use the more powerful library requests library as we
did above.
'''
