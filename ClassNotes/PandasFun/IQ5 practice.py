
import pandas as pd

# Make and label a Series

# make parallel lists and set one to a series in pandas and the other to its header / indexing labels
fruits = ["banana", "apple", "blueberry", "grape", "kiwi"]
colors = ["yellow", "red", "blue", "purple", "green"]

fruits_series = pd.Series(fruits) # makes a Series from a passed in list
print(fruits_series)
print()

# now let's change the indexing so the headers are their colors!
fruits_series = pd.Series(fruits, index=colors)
print(fruits_series)
print()

# name a Series!
# this is awesome if we want to add a column to a dataframe
fruits_series.name = "All My Fruits!"
print(fruits_series)
print()



# Indexing and slicing in a Series
# label based and position based indexing
# label based = uses header to pass in name of header to get values
# position based = uses actual index number 0, 1, 2,... to get values

# LABEL-BASED INDEXING
print(fruits_series["red"]) # will grab value "apple"
print()
print(fruits_series[["yellow", "blue"]]) # use [[ ]] to index to grab more than one value in our Series, returns an object
print()

# label-based slicing operator is INCLUSIVE!
print(fruits_series["blue": "green"]) # goes all the way including green's element, kiwi (blueberry, grape, kiwi), returns an object (blueberry. kiwi)
print()


# POSITION BASED INDEXING
# use .iloc[]
print(fruits_series.iloc[3]) # prints out 3rd index's element, "grape"
print()
print(fruits_series.iloc[[2, 3]]) # use [[ ]] again when grabbing more than one value in Series, returns an object (blueberry, grape)
print()

# .iloc slicing operator is EXCLUSIVE!
print(fruits_series.iloc[1:3]) # includes apple, blueberry, but not grape
print()



# Statistics functions in pandas
customers = [1, 6, 2, 9, 20, 18, 50]
day_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

customers_series = pd.Series(customers, index=day_of_week)
customers_mean = customers_series.mean() # need to apply .mean() to a series in order for it to work
print("customer's mean:", customers_mean)
print(customers_series)
print()

# we can add new data by indexing and replacing at the index
customers_series["monday"] = 99 # modify the SERIES by indexing at its label index and replacing it with a valid value
print(customers_series)
print()

# creating a new empty Series
customers_series2 = pd.Series(dtype=int)
customers_series2["vacation"] = 71
print(customers_series2["vacation"])
print()



# DataFrames

# create a DataFrame and assign it a column (attribute label) and index (row label)
header = ["City", "Population", "Class"]
row_index = ["row1", "row2", "row3", "row4"]

pop_data = [["Spokane", 219190, "Medium"], 
            ["Seattle", 744966, "Large"], 
            ["Bellevue", 147599, "Medium"], 
            ["Leavenworth", 2010, "Small"]]

pop_df = pd.DataFrame(pop_data, columns=header, index=row_index)
print(pop_df)
print()

pop_df = pop_df.set_index("City") # eliminate the row indexes by setting the city column to be the new indexes
print(pop_df)
print()

# indexing and slicing a DataFrame
pop_ser = pop_df["Population"] # cannot index at City because we set it to be the index so it shows up anyways with Population here
print(pop_ser)
print()

# use .iloc[] again to index based on numeric index number
pop_spokane = pop_df.iloc[0, 0] # returns spokane's population because [0,0] is now the population column because City is our index
print("df.iloc[0,0] = ", pop_spokane)
print()

pop_values = pop_df.iloc[0:2] # stop on .iloc[] is EXCLUSIVE
print(pop_values)
print()

# use .loc[] for label based indexing in a DataFrame
pop_spokane = pop_df.loc["Spokane", "Population"] # returns spokane's population
print(pop_spokane)
print()

pop_values = pop_df.loc["Spokane": "Bellevue"] # .loc[] slicing (label based) is INCLUSIVE
print(pop_values)
print()


# let's read a csv file in
regions_df = pd.read_csv("regions.csv")
print(regions_df)
print()

# let's merge the regions_df with our pop_df on the attribute key "City"
merged_df = pop_df.merge(regions_df, on="City")
print(merged_df)

merged_df.to_csv("merged.csv")




# SPLIT APPLY COMBINE METHOD TO GATHER AND SUMMARIZE DATA


# data aggregation: gathering and summarizing data
# split-apply-combine
# 1. split on the "Class" attribute
# use pandas groupby() to do this
grouped_by_class = merged_df.groupby("Class") # .groupby("Class") groups our merged_df by class
print(type(grouped_by_class))
# prints values at Class attribute, large, medium, small (we grouped by class, so that attribute is our key, so use .groups.keys())
print(grouped_by_class.groups.keys()) # .groups.keys() returns the keys in our grouped object
# .get_group("Medium") gets all values matched with attribute from class, medium
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
    mean_pop_ser[group_name] = mean_group_pop # previously made this into a series so we could access it
    print("******")
    print()
print()

print("result of split-apply-combine on Class")
mean_pop_ser.name = "Mean Population"
print(mean_pop_ser)
print()

# shorter way :) 
mean_pop_ser = grouped_by_class["Population"].mean()
print(mean_pop_ser)
print()
print()


mean_group_ser = pd.Series(dtype=float)
for group_name, group_df in grouped_by_class:
    pop_column = group_df["Population"]
    pop_mean = pop_column.mean()
    mean_group_ser[group_name] = pop_mean

print(mean_group_ser)
