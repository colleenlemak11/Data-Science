'''
Programmer: Colleen Lemak
Class: CPSC222, Fall 2020
Data Assignment #2
Date: 9/30/20
I did not attempt the bonus activity
Description: This file calls functions in utils.py to execute various tasks.
'''
import utils

filename = "fitbit_data.csv"

# read data
headers, data = utils.read_data(filename)

# display statistics in grid
utils.display_table(headers, data)

# have user enter an input, and get the column and return its data
print("Enter the column name of the data.")
user_col_name = input()
print()
user_list = utils.get_column(headers, user_col_name, data)
utils.convert_column_to_numeric(user_list)
print("The", user_col_name, "list is:", user_list, "\n")

# compute mean, standard_deviation, median, smallest, largest
utils.print_col_stats(user_list, user_col_name)