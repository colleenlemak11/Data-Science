'''
Programmer: Colleen Lemak
Class: CPSC222, Fall 2020
Data Assignment #1
Date: 9/16/20
I attemptted the bonus activity.
Description: This program computes the count, mean, standard deviation, median number, smallest number, and largest number 
rounded to two decimal places of a list of numbers.  It also prompts the user to enter a start and end value to set all other 
values not in the range to 0.
'''
import math

# initialize list of numbers
list_numbers = [84.4, 75.8, 42.1, 25.9, 51.1, 40.5, 78.4, 30.3, 47.7, 58.3, 90.8, 50.5, 28.2, 75.6, 61.8, 25.1, 91.0]

# count of the numbers
count = len(list_numbers)
print("The count of numbers is: ", count)

# average mean of the numbers
list_numbers_sum = sum(list_numbers)
list_numbers_mean = list_numbers_sum / count
print("The mean of the numbers is: ", round(list_numbers_mean, 2))

# standard deviation of the numbers
# subtract mean and square each term, then find mean of that list and take the square root of it for stand dev
subtract_and_square_list = list_numbers.copy()
i = 0
for i in range (count):
    subtract_and_square_list[i] = subtract_and_square_list[i] - list_numbers_mean
    subtract_and_square_list[i] = subtract_and_square_list[i] ** 2

sas_list_sum = sum(subtract_and_square_list)
sas_list_mean = sas_list_sum / count
sas_standard_dev = sas_list_mean ** (1/2)
sas_standard_dev = round(sas_standard_dev, 2)
print("The standard deviation of the numbers is: ", sas_standard_dev)

# median number of the list
sorted_numbers = sorted(list_numbers)
median_index = (count // 2)
print("The median number is: ", sorted_numbers[median_index])

# smallest number
print("The smallest number is: ", round(sorted_numbers[0], 2))

# largest number
print("The largest number is: ", round(sorted_numbers[count - 1], 2))

# get user data for start and end value input
print("Enter the start value.")
start = float(input())
print("Enter the end value.")
end = float(input())

# new list created with 0s based on range of numbers given
modified_list = list_numbers.copy()
idx = 0
for idx in range (count):
    if modified_list[idx] >= start and modified_list[idx] <= end:
        modified_list[idx] = 0
    modified_list[idx] = round(modified_list[idx], 2)
    idx += 1
print("The modified list is: ", modified_list)

# extra credit: reverse the list without reverse() function
i = 0
j = 0
for i in range(0, count - 1):
    smallest = i
    for j in range(i + 1, count):
        if list_numbers[j] > list_numbers[smallest]:
            smallest = j
    list_numbers[i], list_numbers[smallest] = list_numbers[smallest], list_numbers[i]
print("The reverse ordered list is: ", list_numbers)