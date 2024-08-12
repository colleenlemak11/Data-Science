# Sept 28 Notes

import random

# 10 rows, 5 columns
data = []
for i in range(10):  # runs 10 times
    row = []
    for j in range(5):
        rand_num = random.randint(1, 11)  # random number 1 to 10 inclusive
        row.append(rand_num)
    data.append(row)

print(data)

# print in a grid-like format
for row in data:
    for value in row:
        print(value, end="\t")
    print()

# prints largest and smallest number in list
smallest_num = largest_num = data[0][0]
for row in data:
    # recall: data is 2D so row is 1D
    if min(row) < smallest_num:
        # new smallest
        smallest_num = min(row)
    if max(row) > largest_num:
        # new largest
        largest_num = max(row)
print("smallest:", smallest_num, "largest:", largest_num)

# search for user's number in 2D list
user_num = int(input("Enter a number [1, 10] to count:"))
count = 0
for row in data:
    for num in row:
        if num == user_num:
            count += 1
print("count:", count)

# removes all instances of user-specified number
user_num = int(input("Enter a number [1, 10] to count:"))
found = False
for row in data:
    while user_num in row:
        found = True
        row.remove(user_num)
if found:
    print(data)
else:
    print("Sorry, your number is not in the list")



# rows go horizontally, columns go vertically
# Tabuar Data is data organized into tables (rows x cols)
# each row is an "instance" aka record, object
# each column is an "attribute" aka variable, field, feature
# a data set is a sample set of instances (1 or more tables)
# key: one or more attributes that uniquely identify instances (user ID, row index is a key, it UNIQUELY IDENTIFY ROWS)
# foreign keys: a reference to an instance in another table
# joins: combine 2 tables on any attributes, typically keys/foreign keys
# inner join: make 3rd table only includes rows that match on attributes in both tables
# outer join: include non-matching rows as well (not shared), fill non-matching attribute values with null (NaN = not a number in python)



