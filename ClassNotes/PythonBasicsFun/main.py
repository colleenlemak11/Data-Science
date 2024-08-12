import math 

# SEPT 7 NOTES
# this is a one line comment
# a line of code ignored by Python when it runs the program
# we use comments to document our code

'''
this is a multi line
comment
AKA a block comment

djaidsa
jfjovvc
'''

# VARIABLES
x = 5 # "x is assigned 5", or "x stores 5", NOT "x equals 5"
print(x)
# a variable stores a value
# the value has a "data type" which defines the range of values
# int (short for integer) is a data type that stores integers (whole numbers)
print(type(x))

# let's override x with a new value
x = 5.5
print(x)
print(type(x))

# float is a data type that stores decial numbers (numbers with a fractional decimal part)
x = "hello"
print(x)
print(type(x))
# a string is a data type that stores a sequence of characters

# OPERATORS
# * is multiplication
print(4 * 5)
# / is the floating point division  (this is the "normal" division)
print(5 / 2)
# // is the integer division (this is just the whole number resulting from division)
print(5 // 2) # trunkating, chops off decimal, you get 2
# % is modulus (this is the remainder from the integer division)
print(5 % 2)
# ** is the exponentiation (power)
print(2 ** 5) # returns type of operators
# we have a pow() function for exponentiation, it is in the math module
# we have to "import" the math module
print(math.pow(2, 5)) # returns a float
# control shift P for python interpreter

print("hello world")

# GETTING INPUT FROM THE USER INTERACTIVE :)
print("Enter your favorite number: ")
favorite_number = input() # snake case with under-score, data type is a string
print("Your favorite number is: ", favorite_number)
print("Your favorite number doubled is:", 2 * favorite_number, sep="", end=":):)") # prints out twice because it is a string (2 of these strings), keyword arguments
print(type(favorite_number)) # check its type here using type

# let's say we want favorite number to be a numeric type (int or float)
# this is called type conversion (use for arithmetic)
favorite_number_int = int(favorite_number)
print(type(favorite_number_int))
print("Your favorite number doubled is: ", 2 * favorite_number_int)
