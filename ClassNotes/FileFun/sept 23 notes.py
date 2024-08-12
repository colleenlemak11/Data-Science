# Sept 23 Notes
# FILES
# a file stores data on your file system ("on disk")
# 3 part file processing template
# 1. open the file
# 2. process the file (ex: read or write)
# 3. close the file

# goal: open data.csv in python
# read in its contents
# read in its contents
# store the contents in a list (eventually a 2D list)

# use functions for practice
def load_lines_from_file(filename):
    # filename is a path to a file to open (string)
    # 1. absolute path: start with a drive on Windows (C:\)
    # or root (/)
    # they are unique!
    # example = "/Users/sprint/vscode/filefun/main.py"

    # 2. relative path: doesn't start with a drive or root
    # example: "data.csv" (csv: comma separated value list)
    # relative to the CWD (current working directory, check terminal or VS code)

    # Step 1
    infile = open(filename, "r")  # "r" is the mode for reading
    # Step 2
    lines = infile.readlines()  # reads all lines into a list
    # Step 3
    infile.close()
    return lines

def clean_lines(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

def restructure_data_into_table(lines):
    data = []  # going to be a 2D list
    for line in lines:
        values = line.split(", ")
        # print(values)
        data.append(values)
    return data

def pretty_print(data):
    for row in data:
        for value in row:
            print(value, end=" ")
        print()

def remove_whitespace(data):
    for row in data:
        for i in range(len(row)):
            row[i] = row[i].strip()

def convert_column_to_numeric(data, column_index):
    for row in data:
        row[column_index] = int(row[column_index])  # override the element in data to an int type


lines = load_lines_from_file("data.csv")
# print("lines:", lines)
clean_lines(lines)
print("cleaned lines:", lines)

# we want to restructure the lines into a nested list of values
data = restructure_data_into_table(lines)
print("data:", data)

# task: write a pretty_print() function that prints a 2D list in a grid fashion
'''
id column1 column2
001 monday 14
002 tuesday 7
'''
pretty_print(data)

# task: write a remove_whitespace(data) function and removes the whitespaces
remove_whitespace(data)
print("after removing whitespaces:", data)

# we want to convert column2's data to a numeric type (so we can do arithmetic with it)
header = data.pop(0)
print("header:", header)
print("data:", data)

convert_column_to_numeric(data, 2)
print("after numeric column2:", data)
