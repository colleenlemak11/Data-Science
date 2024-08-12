# Sept 30 Notes

# # Aspects of Attributes
# data storage type: int, float, string...
# measurement scales: categorical scale or continuous scale
# semantic type: what do the values represent? (people, ages, hometown, first marathon)
# noisy or invalud values in data?
# labeled or unlabeled

# measurement scales 4

# Categorical / discrete (whole)
# 1. Nominal: discrete data values without an inherent data ordering (any data type--occupation: accountant, 
#    lawyer, colors: red, green, no second attribute, just a discrete category, not ordered)
# 2. Ordinal--discrete values with an inherent order (any data type, etter grade: A, A-..., t-shirt sizes: S, M, L...)
#    NO guarentee on distance formula between 2 values

# Continuous / numeric (varies can be fractions)
# 3. Interval--values measured on a scale of equal sized widths
#    no inherent zero point (int, float, meaning absence of a value, ex: temperature C or F)
# 4. Ratio--interval values with an inherent 0 point (ex: temperature, weight, height)


# Noisy vs Invalid value
# noisy is valid on the scale, but recorded incorrectly (ex: when asked for a where you live, you say Idaho instead of Washington)
# invalid is not valid on the scale (instead of Washington you enter 1234)


# Labeled vs Unlabeled
# labled data is an attribute that represents a "class", something that can be classified, used for "classification" in supervised
#   machine learning--predict a class value for an unseen instance
# unlabled data is not a class attribute (if data set doen't have a class attribute)
#   unsupervised machine learning--looking/mining for things like patters, groups, relationships

# # pandas is short for panel data
# # it is a library, like numpy, for data science
# # it is built on memory
# # # one of the major shortcomings of using lists
# # # for data science, is the lack of label-based indexing
# # # ex: the header
# # also great builtin functionality for indexing, cleaning, stats, etc

# # there are two main objects in pandas
# # 1D data: pandas Series
# # 2D data: pandas DataFrame (every column is a series)


# OCT 5 NOTES

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
# use loc[] for label-based indexing
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





# SPLIT APPLY COMBINE METHOD TO GATHER AND SUMMARIZE DATA


# data aggregation: gathering and summarizing data
# split-apply-combine
# 1. split on the "Class" attribute
# use pandas groupby() to do this
grouped_by_class = merged_df.groupby("Class")
print(type(grouped_by_class))
print(grouped_by_class.groups.keys())
medium_df = grouped_by_class.get_group("Medium")
print(type(medium_df))
print(medium_df)
# we want to write general, extensible code to process each group
# no matter how many groups there are!
# 2. apply mean() to the "Population" column FOR EACH GROUP
mean_pop_ser = pd.Series(dtype=float)
for group_name, group_df in grouped_by_class:
    print(group_name)
    print(group_df)
    group_pop_ser = group_df["Population"]
    mean_group_pop = group_pop_ser.mean()
    print("mean:", mean_group_pop)
    # 3. combine: combine the means for each class into a single Series
    mean_pop_ser[group_name] = mean_group_pop
    print("******")

print("result of split-apply-combine on Class")
mean_pop_ser.name = "Mean Population"
print(mean_pop_ser)

# shorter way :)
mean_pop_ser = grouped_by_class["Population"].mean()
print(mean_pop_ser)
