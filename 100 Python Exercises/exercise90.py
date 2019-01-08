#Question:
'''
Please download the database file database.db. The file contains a table with
50 country names along with area in square km and population. Please use Python
to print out those countries that have an area of greater than 2,000,000.
Then export those rows to a CSV file

Hint: You can use pandas.DataFrame.from_records
'''
#Answer
'''
import sqlite3
import pandas

conn = sqlite3.connect("database.db")
cur = conn.cursor()
cur.execute("SELECT country FROM countries WHERE area >= 2000000")
rows = cur.fetchall()
conn.close()

df = pandas.DataFrame.from_Records(rows)
df.columns = ["Rank", "Country", "Area", "Population"]
df.to_csv("countries_big_area.csv", index = False)
'''
