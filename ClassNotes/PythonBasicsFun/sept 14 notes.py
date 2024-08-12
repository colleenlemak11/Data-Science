# Sept 14 Notes
# q = k * A * (T1 - T2) / L  (have to put in * between A and (T1 - T2))

import math
import random  # import if need random numbers

# IF STATEMENTS CONT.
# we also have an else keyword
# that we can attach to an if structure
# else bodies only execute when the condition on the associate if it is false
x = 10
if x == 6:
    print("x is 6")
else: # x == 6 is false, so x != 6
    print("x is NOT 6")

# we also have an elif (else if)
# use elif when you want to test multiple conditions in order
# the first one that evaluates to true, will have its body execute 
# then an exit from the entire if structure
x = 5
if x < 0:
    print("x is negative")
elif x > 0: # only executes when x is not < 0 so x >=0
    print("x is positive")
else: # executes when all previous conditions are false (catch all)
    print("x is 0")

# you can nest if statements (pay attention to indentation)


# LOOPS
# there are for loops and while loops
# both are used repeating statements

# for loop structure
# for item in sequence: 
#   statements to be repeated (ex: the body of the loop)
#   do something with the item
# lots of sequences we can use for loops
# lists are sequences! (called arrays in c++)
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

# strings are sequences! (sequence of characters)
for character in "hello":
    print(character)

# we can generate our sequences using range()
# for i in range(start, stop):  # generates a sequence [start, stop)
for i in range(4, 9):  # [4, 9) meaning [4, 8], start inclusive, end is exclusive
    print(i, end = " ")  # replace automatic new line with space at the end of each item
print()

# for i in range(start, stop, step):  # generates a sequence [start, stop, step]
for i in range(4, 9, 2):  # [4, 9) meaning [4, 8], going up by two, skips lines
    print(i, end = " ")  # replace automatic new line with space at the end of each item
print()

# try printing out the previous nubers in reverse: 8 6 4
# task: Write a for loop to print the first 20 even numbers all on one line
# separated by a comma and a space (2, 4, ... 38, 40) last number ends without comma
print("My code is here!")
for i in range (2, 40, 2):  # stop one early and print last item without comma
    print(i, end = ", ")
print(i + 2)

# while loop structure
# while condition is true:
#   body of statements to be repeated
#   progress toward condition being false (otherwise you have an infinite loop)
k = 2  # loop control variable
while k <= 38:
    print(k, end = ", ")
    # don't forget progress towards k > 38
    k += 2
print(k)
# hit control C to stop program, keyboard interrupt


# ADVANCED LOOPS
# like if statements you can nest loops
# you can get an early exit from a loop using break keyword
# True False are keywords
# while True will give an infinite loop, while False will never run
# while True:
#     user_input = input("Enter a word (stop to quit): ")
#     if user_input == "stop":
#         break
# print("here")

# control / to block comment out or uncomment code

# RANDOM NUMBERS
# often we need a "random" number to simulate something or to set up the 
# starting state of algorithm
# CPSC 322 Data Science Algorithms
# import the random module
# let's throw a 6-sided die

# if you want the same results, you can seed the generator with a constant
# this is nice for reproducabiity
random.seed(0)

die_roll = random.randrange(1, 7)  # [1, 7) which is [1, 6]
print("die_roll:", die_roll)

die_roll = random.randint(1, 6)  # [1, 6] use randint
print("die_roll:", die_roll)


# FUNCTIONS
# a named sequence of statements
# ex: round(), print(), input(), etc...
# we are going to write our own
# functions take inputs() (called arguments when you "call" the function, and parameters 
# when you define function)
# functions produce outputs (return values AKA results)
# def is a keyword that prompts function
# def function_name(parameter list):
#   function body (statements that execte when the function is "called")
# calling a function means to execute it
# reasons to use functions: reusability (define once, call multiple times)
# also for organization

