'''
Programmer: Colleen Lemak
Class: CPSC222, Fall 2020
Data Assignment #4
Date: 10/21/21
I did not attempt the bonus activity.
Description: This program uses json and requests to execute assignment.
'''

import requests
import json
import pandas as pd
from datetime import date

# API information
headers = {"x-rapidapi-key": "af4a613410msh971f8b7dfec91afp182423jsncb2deddc7ff9"}
mapquest_url = "http://open.mapquestapi.com/geocoding/v1/address"
map_quest_api_key = "yzaGHHCwd14UflR663zZj2xOEA5L4861"
meteostat_url = "https://meteostat.p.rapidapi.com/stations/nearby"
meteostat_api_key = "af4a613410msh971f8b7dfec91afp182423jsncb2deddc7ff9"
weather_url = "https://meteostat.p.rapidapi.com/stations/daily"
weather_api_key = "af4a613410msh971f8b7dfec91afp182423jsncb2deddc7ff9"

# get user's city name
user_city_name = input("Enter the name of a large city. ")
user_city_name = user_city_name.replace(" ", "+")


# MAPQUEST
# include key and name in mapquest url 
mapquest_url += "?key=" + map_quest_api_key + "&city=" + user_city_name

# request and obtain lat and lng from mapquest
response = requests.get(url=mapquest_url)
json_object = json.loads(response.text)

results_arr = json_object["results"]
locations_arr = results_arr[0]["locations"]
latLng = locations_arr[0]["latLng"]

lattiude = latLng["lat"]
longitude = latLng["lng"]

print("Lattitude is:", lattiude, "\nLongitude is:", longitude)
print()


# METEOSTAT
# include key and name in meteostat url
meteostat_url += "?rapidapi-key=" + meteostat_api_key + "&lat=" + str(lattiude) + "&lon=" + str(longitude)

# request and obtain weather ID from meteostat
response = requests.get(url=meteostat_url)
json_object = json.loads(response.text)

results_arr = json_object["data"]
id_arr = results_arr[0]["id"]


# DAILY WEATHER
today = date.today()
weather_url += "?rapidapi-key=" + weather_api_key + "&station=" + str(id_arr) + "&start=" + "2021-01-01" + "&end=" + str(today)

# request weather stats from daily weather, store in df
response = requests.get(url=weather_url)
json_object = json.loads(response.text)
response_df = pd.DataFrame(json_object["data"])

# convert to F from C degrees
def convert_celcius_to_fahrenheit(col_name):
    for i in range(len(response_df)):
        celcius = response_df.at[i, col_name]
        fahrenheit = round((celcius * (9/5) + 32), 1)
        response_df.at[i, col_name] = fahrenheit

# convert tavg, tmin, tmax columns
convert_celcius_to_fahrenheit("tavg")
convert_celcius_to_fahrenheit("tmin")
convert_celcius_to_fahrenheit("tmax")

# write daily weather stats to csv file
response_df.to_csv(user_city_name + "_daily_weather.csv")
print(response_df)
print()

# remove columns with > 75% missing data
weather_cols = ["tavg", "tmin", "tmax", "prcp", "snow", "wdir", "wspd", "wpgt", "pres", "tsun"]
for value in weather_cols:
    if response_df[value].isnull().sum() // 291 > 0.75:
        response_df.drop(value, 1, inplace=True)

# fill remaining missing values
interpolated_response_df = response_df.interpolate()
interpolated_response_df.fillna(method="ffill")
interpolated_response_df.fillna(method="bfill")

# write cleaned df to csv file
interpolated_response_df.to_csv(user_city_name + "_daily_weather_cleaned.csv")
print(response_df)
print()
