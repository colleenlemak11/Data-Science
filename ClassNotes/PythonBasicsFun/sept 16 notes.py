# Sept 16 Notes
# help(print)  # doc-string is printed

import math
import random

# EXAMPLE 1: no parameters (call the function, you don't pass any arguments, and no return value)
def say_hello():
    print("hello!")

# the body of say_hello() only executes when we call the function
say_hello()  # function call, prints out "hello!"

for i in range(2):  # prints it out twice
    say_hello()


# EXAMPLE 2: one parameter (call the function, we need to supply one argument) and no return value
def say(message):
    print(message)

say("go zaGs!")


# TASK: define and call a function that accepts the radius of a circle
# print the area of the circle
def compute_circle_area(radius):
    area = math.pi * (radius ** 2)
    print("area:", area)

compute_circle_area(5.0)


# EXAMPLE 3: one parameter, one return value
# resolve the previous task, but return the area to the calling code
def compute_circle_area2(radius):
    area = math.pi * (radius ** 2)
    return area

result = compute_circle_area2(5.0)
print("result:", result)


# EXAMPLE 4: one parameter, two return values
def compute_circle_area_and_circumference(radius):
    area = math.pi * (radius ** 2)  # area ony has local scope to this specific function
    circumference = 2 * math.pi * radius
    return area, circumference

result1, result2 = compute_circle_area_and_circumference(5.0)
print("result1:", result1, "result2:", result2)


# 1D LIST PRACTICE PROBLEMS
# 20 random numbers in a 1D list
numbers = []
for i in range(20):  # repeat 20 times, don't need i variable 
    numbers.append(random.randrange(1, 11))  # random.randrange[) inclusive of first, exclusive of second
print("numbers:", numbers)

# prints the numbers all one line, each number separated by a space
def pretty_print(numbers):
    for num in numbers:
        print(num, end=" ")  # add a space in between
    print()  # put so it will give newline

pretty_print(numbers)

# sorts the list using a list method
# numbers.sort()  # in place sort, changes the order in memory
numbers_copy = sorted(numbers)  # makes a copy without changing original list
pretty_print(numbers_copy)

# prints the largest and smallest number in the list
print("min:", numbers_copy[0], "max:", numbers_copy[19])
print("min:", min(numbers), "max:", max(numbers))

# determines the number of lines a user-specified number is in the list
user_num = int(input("Please enter a number in [1, 10] to count:"))
count = 0
for num in numbers:
    if num == user_num:
        count += 1
        
print("count:", count)

# removes instances of a user-specified number in the list
user_num = int(input("Please enter a number in [1, 10] to remove:"))
if not user_num in numbers:
    print("Sorry your nuuber is not here!")
else:  # user_num is in numbers
    while user_num in numbers:
        numbers.remove(user_num)
print(numbers)
