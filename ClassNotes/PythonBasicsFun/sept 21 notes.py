# Sept 21 Notes

import math

# warm up task
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]

def list_checker(list1, list2):
    same_first = False
    same_last = False

    if(len(list1) > 0 and len(list2) > 0):
        if list1[0] == list2[0]:
            same_first = True
        if list1[-1] == list2[-1]:
            same_last = True
    return same_first, same_last

print(list_checker(list1, list2))


# (more on) LIST METHODS
winter = ["snow", "christmas"]
print(winter)
# append()
winter.append("cocoa")
print(winter)
# extend()
winter.extend(["ski", "sledding"])
print(winter)
# +=
winter += ["frost", "santa"]
print(winter)

# pop() like remove(), but pass in an index instead
first_word = winter.pop(0)
print(first_word, winter)

# creating a string for a list of strings
# join(), concatanate
sledding_list = ["sl", "e", "dd", "i", "n", "g"]
sledding_str = "".join(sledding_list)
print(sledding_str)

# creating a list from a string
sledding_list2 = list(sledding_str)
print(sledding_list2)

comma_separated_list_of_values = "a*,*b*,*c*,*d"  
# comma is delimiter, separates values
values_list = comma_separated_list_of_values.split("*,*")  # detects this parameter as a time to split it up
print(values_list)

# LIST ALIASING
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1, list2)
list1[0] = 100
print(list1, list2)

list3 = list1 # list is alias, not a copy!
print(list1, list2, list3)
list3[0] = 200
print(list1, list2, list3)

# lists (and objects) are "pass by object reference"
# this means, if you pass a list (or an object) to a function
# and that function modifies the list, the modification persists
def add_one_to_each_element(some_list):  # alias is some_list
    for i in range(len(some_list)):
        some_list[i] += 1  # modifies the list passed in!! 

add_one_to_each_element(list1)
print(list1, list2, list3)

# (more on) STRINGS
word = "winter"
print(word)
# 0-based indexing
print(word[0], word[-1], word[2:4])
# strings are immutable (they cannot be changed)
# word = "W" would not work

# string concatenation operator +
word = "winds of " + word
print(word)

# repition operator *
print(word * 5)

# string comparison < <= > >= == !=
# comparison is character by character using ASCII codes (integer values assigned to characters)
print("clash of kings" < word)  # c has a smaller ASCII code than w, so it is True
# a is ASCII 97, c is 99
# A is ASCII 65
print("Winds of winter" < word)

# STRING METHODS
# join(), lower(), strip(), find(), etc...
# strip() to remove leading and trailing whitespace characters
word = "    \n          \t      winter        \t\t\t\t  \n"
print(word)
word = word.strip()
print(word)

# find() returns the index of the string if it is found, -1 otherwise (.lower() on strings for lowercase)
print(word.find("in"))  # gives me index 1
