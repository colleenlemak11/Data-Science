'''
Programmer: Colleen Lemak
Class: CPSC222, Fall 2020
Data Assignment #2
Date: 9/30/20
I did not attempt the bonus activity
Description: This file creates functions to compute the mean, standard deviation, median number, smallest number, and largest number 
rounded to two decimal places of a list of numbers.  It also implements functions which use files to read in data.
'''
import math

def compute_mean_standard_dev_median_smallest_largest(list_numbers):
    # compute mean
    count = len(list_numbers)
    list_numbers_sum = sum(list_numbers)
    list_numbers_mean = list_numbers_sum / count
    list_numbers_mean = round(list_numbers_mean, 2)

    # compute standard deviation
    standard_dev_list = list_numbers.copy()
    i = 0
    for i in range (count):
        standard_dev_list[i] = standard_dev_list[i] - list_numbers_mean
        standard_dev_list[i] = standard_dev_list[i] ** 2

    sd_sum = sum(standard_dev_list)
    sd_mean = sd_sum / count
    standard_deviation = sd_mean ** (1/2)
    standard_deviation = round(standard_deviation, 2)

    # compute median
    sorted_numbers = sorted(list_numbers)
    median_index = (count // 2)
    median = round(sorted_numbers[median_index], 2)

    # find smallest number
    smallest = round(sorted_numbers[0], 2)

    # find largest number
    largest = round(sorted_numbers[count - 1], 2)

    return list_numbers_mean, standard_deviation, median, smallest, largest

def read_data(filename):
    infile = open(filename, "r")
    lines = infile.readlines()
    clean_lines(lines)
    data = restructure_data_into_table(lines)
    headers = data.pop(0)
    infile.close()
    return headers, data

def clean_lines(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

def restructure_data_into_table(lines):
    data = []  # going to be a 2D list
    for line in lines:
        values = line.split(",")
        data.append(values)
    return data

def display_table(headers, data):
    for i in headers:
        print(i, end="    ")
    print("\n")
    for row in data:
        for i in row:
            print(i, end="\t\t")
        print("\n")
    print()

def convert_column_to_numeric(list_numbers):
    for i in range(len(list_numbers)):
        list_numbers[i] = float(list_numbers[i])  # override the element in data to an int type

def get_column_index(headers, col_name, data):
   for i in range (len(headers)):
       if col_name == headers[i]:
           return i

def get_column(headers, col_name, data):
    col_index = get_column_index(headers, col_name, data)
    col_list = []
    for row in data:
        col_list.append(row[col_index])
    return col_list 

def print_col_stats(col_list, col_name):
    mean, standard_deviation, median, smallest, largest = compute_mean_standard_dev_median_smallest_largest(col_list)
    print("The", col_name, "list statistics:\nmean is:", mean, "\nstandard deviation is:", standard_deviation, "\nmedian is:", median, "\nsmallest number is:", smallest, "\nlargest number is:", largest, "\n")

