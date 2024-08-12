'''
Programmer: Colleen Lemak
Class: CPSC222, Fall 2020
Data Assignment #3
Date: 10/14/20
I did not attempt the bonus activity.
Description: This program uses pandas to perform varies tasks with files.
'''

import pandas as pd

# read lines of youtube file into df
youtube_file = pd.read_csv("youtube_analytics_9-20-20_9-20-21.csv", index_col="Date")
youtube_df = pd.DataFrame(youtube_file)

# read lines of days file into df
days_file = pd.read_csv("days_of_week_9-20-20_9-20-21.csv", index_col="Date")
days_df = pd.DataFrame(days_file)

# prompt user for statistics start and end date
start_date = input("Enter an inclusive start date for data. Example: 9/20/20. ")
end_date = input("Enter an inclusive start date for data. Example: 10/11/20. ")

# slice to get data in user's provided time frame
sliced_youtube_df = youtube_df[start_date: end_date]
print("sliced youtube_df\n", sliced_youtube_df)

# store column of data from user's provided column name in series
user_col_name = input("Enter the name of the numeric column for data. The choices are Views, Average percentage viewed (%), Unique viewers, Subscribers, Watch time (hours), Shares, Likes, Dislikes, Comments added, Impressions, Impressions click-through rate (%). ")
user_series = pd.Series(sliced_youtube_df[user_col_name])
print("user series\n", user_series)

# compute stats on user's series
mean = user_series.mean()
sum = user_series.sum()
stand_dev = user_series.std()
median = user_series.median()
min = user_series.min()
max = user_series.max()

# write user's Summary Stats to csv file
user_stats_list = {'mean': mean, 'sum': sum, 'standard deviation': stand_dev, 'median': median, 'minimum': min, 'maximum': max}
user_stats_series = pd.Series(user_stats_list)
user_stats_series.name = "Summary Stats"
print(user_stats_series)
user_stats_series.to_csv("user_stats_series.csv")

# merge youtube df and days df on Date
merged_df = youtube_df.merge(days_df, on="Date")
merged_df.to_csv("merged_df.csv", float_format="%.2f")

# split
grouped_by_day = merged_df.groupby("Day of Week")

# apply
mean_group_series = pd.Series(dtype=float)

for group_name, group_df in grouped_by_day:
    print(group_name)
    group_user_series = group_df[user_col_name]
    mean_group = group_user_series.mean()
    # combine
    mean_group_series[group_name] = mean_group

# write new series with means in column to csv file
mean_group_series.name = "Mean Statistics By Day"
mean_group_series.to_csv("mean_group_user_series.csv", float_format="%.2f")
