#Question:
'''
Create a script that uses the attached countries_by_area.txt file as data
source and prints out the top 5 most densely populated countries

Hint 1: Use pandas.

Hint 2: Once you load the data as a pandas dataframe, create a new column that
is equal to the population column divided by the area column. Then use
sort_values to sort the dataframe by density.
'''
#Answer:
'''
import pandas

data = pandas.read_csv("countries_by_area.txt")
data["density"] = data["population_2013"] / data["area_sqkm"]
data = data.sort_values(by="density", ascending=False)

for index, row in data[:5].iterrows():
    print(row["country"])

Explanation:

We're using pandas to load the data as a dataframe and then calculate a density
column in line 4. Then we use sort_values  to sort the data by density in
descending order. Lastly in the last two lines we access the first
5 rows of the dataframe and iterate using iterrows.
'''
