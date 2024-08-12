'''
Programmer: Colleen Lemak  
Class: CPSC222, Fall 2021  
Quantified Self Project  
Date: 12/06/21    
Description: This file uses Python to execute various utility tasks.
'''
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# loads and stores csv data
def load_and_store_data(filename):
    data = pd.read_csv(filename)
    data_df = pd.DataFrame(data)
    return data_df

# cleans csv data
def clean_data(df):
    interpolated_df = df.interpolate()
    cleaned_df = interpolated_df.fillna(method="ffill")
    cleaned_df = cleaned_df.fillna(method="ffill")
    return cleaned_df

# computes 95% confidence interval
def compute_conf_interval(list_numbers, t_critical):
    Xbar = np.mean(list_numbers)
    stdev = np.std(list_numbers, ddof=1)
    n = len(list_numbers)
    margin_of_error = t_critical * stdev / np.sqrt(n)
    conf_interval = (round(Xbar - margin_of_error, 2), round(Xbar + margin_of_error, 2))
    print("Margin of error:", round(margin_of_error, 2))
    print("We are 95% confident the population mean (number of minutes slept each night) is in", conf_interval)
    return Xbar, conf_interval

# visualize confidence interval
def visualize_conf_interval(Xbar, conf_interval, title):
    plt.plot([1], [Xbar], color="purple", marker="o")
    plt.plot([1, 1], conf_interval, color="purple")
    plt.xticks([1], [title])
    plt.show()

# computes and visualizes 95% confidence interval
def compute_and_visualize_conf_interval(list_numbers, t_critical, title):
    Xbar, conf_interval = compute_conf_interval(list_numbers, t_critical)
    visualize_conf_interval(Xbar, conf_interval, title)

# visualizes sleep bar chart
def sleep_bar_chart(list_numbers, graph_label, title, num):
    x = list(range(len(list_numbers)))
    plt.figure()
    plt.bar(x, list_numbers, facecolor="blue", edgecolor="blue", label=graph_label)
    plt.xticks([num], ["Our timeframe"])
    print(list_numbers)
    plt.title(title)
    plt.legend()
    plt.show()

# prints min and max values of a column
def compute_min_and_max(list_numbers):
    list_numbers = pd.Series(list_numbers)
    max = list_numbers.max()
    min = list_numbers.min()
    print("The maximum minutes of sleep was", max, "minutes, or", round(max/60, 2), "hours.")
    print("The minimum minutes of sleep was", min, "minutes, or", round(min/60, 2), "hours.")

# collects restful minutes column of specific day of the week
def get_restful_minutes(merged_df, day_of_week):
    col_values = []
    for i in range(len(merged_df)):
        if merged_df.at[i, "Day of the Week"] == day_of_week:
            col_values.append(merged_df.at[i, "Restful Minutes"])
    return col_values

# averages values in two columns to create new one
def append_two_cols(col_one, col_two):
    new_col = []
    for i in range(len(col_two)):
        new_col.append(col_one[i])
        new_col.append(col_two[i])
    return new_col

# prints and averages a list
def print_and_average(list, title):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    avg = sum / len(list)
    print(title, "average minutes:", round(avg, 2), "  average hours:", round(avg / 60, 2))

# creates file with Y or N values based on if I got more sleep TTh or MW
def write_yes_or_no_values(mon_wed, tues_thurs):
    comparison_values = []
    for night in range(len(mon_wed)):
        if mon_wed[night] > tues_thurs[night]:
            comparison_values.append("Y")
        else:
            comparison_values.append("N")
    return comparison_values
