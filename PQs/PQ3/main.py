'''
Colleen Lemak
PQ3

three commonly used "built in" data structures
1. list
2. tuple
3. dictionary
'''

# a list is a sequence of items
# 0-based for indexing
# lists are mutable -- they can be changed
# lists have an order to their items
#       0  1  2   3  4  5
#     -len ...      -2 -3
nums = [3, 6, -1, 7, 9, 7]  # can be mixed types
print(nums)
print(nums[0], nums[-6], nums[0:2])  # nums[0:2] slice operator slices 0 inclusive to 2 exclusive

# append an item, adds to back
nums.append(100)
print(nums)

# remove an item, specify number in ()
nums.remove(7)
print(nums)

# in place sort low to high
nums.sort()
print(nums)

# 1D lists (line-like)
# 2D lists (grid-like)
# 3D lists (cube-like)
# 4D-ND lists ... (not preferred)

# 2D lists
# there are two main ways to think about 2D lists
# 1. like a table (it has rows and columns, [row][col])
matrix = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]  # can have different formatting, just helps programmer
print(matrix[0][0])
print(matrix[1][2])
# a 1D list where each item is a 1D list (nested lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(type(matrix[0]))  # list
print(type(matrix[0][0]))  # integer

# 3D lists
cube = [[[0, 0], [1, 1]], [[2, 2], [3, 3]]]
print(cube[0][0][0])

# tuples
# a tuple is an immutable list (cannot be changed)
my_tuple = "x", "y", "z"
print(my_tuple)
print(type(my_tuple))
# my_tuple[0] = "X"  # cannot assign new values

# when declaring a single item tuple, you have to have a comma after it
my_single_item_tuple = (1,)
print(my_single_item_tuple)

# to create an empty tuple
my_empty_tuple = tuple()
print(my_empty_tuple)

# tuple indexing and slicing is the same as for lists
# tuples are used for returning multiple values
# good for when using fixed values

# dictionaires
# a dictionary is a list with keys and indexes and values mapped from those keys

# a key value pair
# use a key to look up a value
# keys in a dictionary must be unique, no duplicates
# example of key: student ID number
# example of a value: student name
# look up ID 12345 -> "Jane Doe"
my_dict = {}  # empty dictionary
my_empty_dict = dict()
print(my_dict)

my_dict["12345"] = "Jane Doe"  # insert into dictionary
print(my_dict)

state_capitals = {"Washington": "Olympia", "Idaho": "Boise", "Oregon": "Portland"}
print(state_capitals)

# dictionaries are mutable
# state_capitals["Washington"] = "Spokane"

# add another state capital
state_capitals["California"] = "Sacremento"
print(state_capitals)

# the key value pairs in a dictionary are not ordered
# initialize a dict using a list of tuples
roman_numerals = dict([("I",  1), ("V", 5), ("X", 10), ("L", 50)])  # key value pairs, structed as tuple
print(roman_numerals)

roman_numerals_as_list = list(roman_numerals.items())
print(roman_numerals_as_list)

# types for keys: integers, strings, files, tuples, etc.
# lists cannot be keys because they can change
# types for values: any type
print(len(state_capitals))

# check for existence of a key
print("Washington" in state_capitals)
print("Olympia" in state_capitals.values())  # .keys() returns key values

# loop through the key value pairs in a dictionary
for state in state_capitals:  # no order in dictionary
    print(state, state_capitals[state])

for (state, capital) in state_capitals.items():
    print(state, "*", capital)



