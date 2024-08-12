import pandas as pd
from pandas.core.reshape.merge import merge

# pandas is short for panel data
# it is a library, like numpy, for data science
# it is built on numpy

# one of the major shortcomings of using lists
# for data science, is the lack of label-based indexing
# e.g. the header!!
# also really great builtin functionality for indexing, cleaning,
# stats, etc....

# there are two main objects in pandas
# 1D data: pandas Series
# 2D data: pandas DataFrame (every column is a series)

# lets start with Series
# there a few ways to make a Series
populations = [219190, 744955, 147599, 2010] # these are parallel lists
cities = ["Spokane", "Seattle", "Bellevue", "Leavenworth"]
pop_ser = pd.Series(populations)
print(pop_ser)
print()
pop_ser = pd.Series(populations, index=cities)
print(pop_ser)
# we can name a Series
# this is really nice if we add the Series as a column to a DataFrame
pop_ser.name = "Population"
print(pop_ser)

# indexing/slicing
# we can use a label to index into the Series and get a value
print(pop_ser["Seattle"])
print(pop_ser[["Seattle", "Leavenworth"]])
print(pop_ser["Seattle": "Leavenworth"]) # stop is inclusive!!!

# we can still do position based indexing
# use .iloc[]
print(pop_ser.iloc[1])
print(pop_ser.iloc[[1, 3]])
print(pop_ser.iloc[1:3]) # stop is exclusive!!

# summary stats
print(pop_ser.mean())
print(pop_ser.std())

# can add new data to a series, just like we add a new key-value pair to a dictionary
pop_ser["Pullman"] = 34019
print(pop_ser)

# we can create an empty Series
pop_ser2 = pd.Series(dtype=int)
pop_ser2["Pullman"] = 34019
print(pop_ser2)

# dataframes
# dataframes are used to store 2D data in pandas
# can make a dataframe from a 2D list
twod_list = [[3, "a", 4.5], [7, "b", 10.99], [-10, "c", -1.5]]
header = ["col1", "col2", "col3"]
df = pd.DataFrame(twod_list)
print(df)
df = pd.DataFrame(twod_list, columns=header)
print(df)

# the column labels are called "columns"
# the row labels are called "index"
row_index = ["row1", "row2", "row3"]
df = pd.DataFrame(twod_list, columns=header, index=row_index)
print(df)

# task: create pop_df
# dataframe for the population data
# 3 columns: 
# 219190, 744955, 147599, 2010
# "Medium", "Large", "Medium", "Small"
header = ["City", "Population", "Class"]
pop_data = [["Spokane", 219190, "Medium"], 
            ["Seattle", 744966, "Large"], 
            ["Bellevue", 147599, "Medium"], 
            ["Leavenworth", 2010, "Small"]]
pop_df = pd.DataFrame(pop_data, columns=header)
print(pop_df)
pop_df = pop_df.set_index("City")
print(pop_df)

# indexing/slicing
# grab a column by its label (returns a series)
pop_ser = pop_df["Population"]
print(pop_ser)
pop_ser = pop_df.iloc[0]
print(pop_ser)
pop_spokane = pop_df.iloc[0, 0]
print(pop_spokane)
# use .loc[] for label-based indexing
pop_spokane = pop_df.loc["Spokane", "Population"]
print(pop_spokane)
# slice across columns with more than one column returns a dataframe

# lets open regions.csv and store the data in a dataframe
regions_df = pd.read_csv("regions.csv", index_col=0)
print(pop_df)
print(regions_df)

# let's join pop_df and regions_df on the attribute (which is the key in both)
# "City"
# to produce a third dataframe (merged_df)
merged_df = pop_df.merge(regions_df, on="City") # by default, inner join
print(merged_df)

# we can write dataframes (and series) to files
merged_df.to_csv("merged.csv")