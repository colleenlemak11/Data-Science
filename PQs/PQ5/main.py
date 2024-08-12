# PQ5 Notes

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pandas as pd
import numpy as np

fname = r"pd_hoa_activities.csv"
df = pd.read_csv(fname, header = 0)
print(df.shape)
print("Number of participants:", df.shape[0] // 9)

print(df.head(n = 5))
print(df.tail(n = 5))
print(df[660:770])
print(df[7:10])
print(df[25:28])

print(df["duration"].value_counts()["?"])

df.replace("?", np.NaN, inplace = True)

for col in df.columns:
    ser = df[col]
    print(ser.value_counts())
    print("Number of NaN:", ser.isnull().sum())
    print("******************************************************\n")

print("Before cleaning:", df.shape)
df.dropna(inplace=True)
index = np.arange(0, len(df))
df.set_index(index, inplace=True)
print("After cleaning:", df.shape)

task_decoder = {"1": "Water Plants", "2": "Fill Medication Dispenser", "3": "Wash Countertop", \
                "4": "Sweep and Dust", "5": "Cook", "6": "Wash Hands", "7": "Perform TUG", \
                "8": "Perform TUG w/Questions", "dot": "Day Out Task"}

def decode_task(df):
    '''
    
    '''
    ser = df["task"]
    for key in task_decoder:
        ser.replace(key,task_decoder[key], inplace = True)

decode_task(df)
print(df.head(n=11))

print(df["duration"].dtype)
print(df["age"].dtype)

df["duration"] = df["duration"].astype(np.int)
print(df["duration"].dtype)

def clean_class(df):
    ser = df["class"].copy()

    for i in range(0, len(ser), 1):
        curr = str(ser[i])
        curr = curr.lower()
        if "hoa" in curr or "healthy" in curr:
            ser[i] = "HOA"
        elif "pd" in curr or "parkinson" in curr:
            ser[i] = "PD"
        else:
            print("Unrecognized status: %d, %s" %(i, ser[i]))
            ser[i] = np.NaN
    df["class"] = ser
clean_class(df)
print(df.head())
print(df["class"].value_counts())

out_fname = r"pd_hoa_activities_cleaned.csv"
df.to_csv(out_fname, index=False)


# # %matplotlib inline
# import matplotlib.pyplot as plt
# import matplotlib.mlab as mlab
# import pandas as pd
# import numpy as np

# # load the data
# fname = r"files\pd_hoa_activities.csv"
# df = pd.read_csv(fname, header=0)
# print(df.shape)
# print("Number of participants:", df.shape[0] // 9)

# # explore the data
# print(df.head(n=5))  # first 5 rows
# print(df.tail(n=5))  # last 5 rows
# print(df[660:6701])  # print rows from 660 to 6701
# print(df[7:10])
# print(df[25:28])

# print(df["duration"].value_counts()["?"])

# # missing data
# df.replace("?", np.NaN, inplace=True)

# for col in df.columns:
#     ser = df[col]
#     print(ser.value_count())
#     print("Number of NaN:", ser.isnull().sum())  # number of NaNs
#     print("*****************************************\n")

# print("Before cleaning:", df.shape)
# df.dropna(inplace=True)
# index = np.arrange(0, len(df))
# df.set_index(index, inplace=True)
# print("After cleaning:", df.shape)

# # decode task
# task_decoder = {"1": "Water Plants", "2": "Fill Medication Dispenser", "3": "Wash Countertop", "4": "Sweep and Dust", "5": "Cook", "6": "Wash Hands", "7": "Perform TUG", "8": "Perform TUG w/Questions", "dot": "Day Out Task"}

# def decode_task(df):
#     '''
    
#     '''
#     ser = df["task"]
#     for key in task_decoder:
#         ser.replace(key, task_decoder[key], inplace=True)
# decode_task(df)
# print(df.head(n=11))

# print(df["duration"].dtype)
# print(df["age"].dtype)

# df["duration"] = df["duration"].astype(np.int)
# print(df["duraiton"].dtype)

# def clean_class(df):
#     '''
    
#     '''
#     ser = df["class"].copy()

#     for i in range(0, len(ser), 1):
#         curr = str(ser[i])
#         curr = curr.lower()
#         if "hoa" in curr or "healthy" in curr:
#             ser[i] = "HOA"
#         elif "pd" in curr or "parkinson" in curr:
#             ser[i] = "PD"
#         else:
#             print("Unrecognized status: %d, %s" %(i, ser[i]))
#             ser[i] = np.NaN
#     df["class"] = ser

# clean_class(df)
# print(df.head())
# print(df["class"].value_counts())

