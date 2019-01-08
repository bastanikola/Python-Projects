#Question:
'''
Please download the database file database.db and the ten_more_countries.txt
file. Then, add the rows of the text file to the database file.

Hint: You need to use the SQL insert method here.
'''
#Answer:
'''
import sqlite3
import pandas

data = pandas.read_csv("ten_more_countries.txt")

conn = sqlite3.connect("database.db")
cur = conn.cursor()

for index, row in data.iterrows():
    print(row["Country"], row["Area"])
    cur.execute("INSERT INTO coutries VALUES (NULL,?,?,NULL)",(row["Country"], row["Area"]))
conn.commit()
conn.close()
'''
