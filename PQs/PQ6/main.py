# Colleen Lemak
# PQ 6

import json
import pandas as pd

# JSON: javascript object notation
# a data format using key/value pairs
# like a dictionary
# key (AKA name): string
# e.g. "id"
# value: number (ex: 1234), string (ex: 1234AZ), array (ex: [1, 2, 3, 4])
# boolean (ex: true), a JSON object (ex: nesting)

# ex: {"id": 1234}
# ex: {"id": {"name": "jane", "age": 20}

json_arry_str = """
[
    {
      "TimestampUTC": "2020-03-24T00:27:00Z",
      "TimestampSubjectTZ": "2020-03-23T20:27:00",
      "Calories": 0.0234859050963356,
      "HR": 0.0,
      "Lux": null,
      "Steps": 0.0,
      "Wear": true,
      "x": 0,
      "y": 35,
      "z": 0,
      "AxisXCounts": 0,
      "AxisYCounts": 35,
      "AxisZCounts": 0
    },
    {
      "TimestampUTC": "2020-03-24T00:28:00Z",
      "TimestampSubjectTZ": "2020-03-23T20:28:00",
      "Calories": 0.042274629173404,
      "HR": 0.0,
      "Lux": null,
      "Steps": 0.0,
      "Wear": true,
      "x": 44,
      "y": 63,
      "z": 55,
      "AxisXCounts": 44,
      "AxisYCounts": 63,
      "AxisZCounts": 55
    },
    {
      "TimestampUTC": "2020-03-24T00:29:00Z",
      "TimestampSubjectTZ": "2020-03-23T20:29:00",
      "Calories": 0.0,
      "HR": 0.0,
      "Lux": null,
      "Steps": 0.0,
      "Wear": true,
      "x": 0,
      "y": 0,
      "z": 0,
      "AxisXCounts": 0,
      "AxisYCounts": 0,
      "AxisZCounts": 0
    },
    {
      "TimestampUTC": "2020-03-24T00:30:00Z",
      "TimestampSubjectTZ": "2020-03-23T20:30:00",
      "Calories": 0.224122637205031,
      "HR": 0.0,
      "Lux": null,
      "Steps": 0.0,
      "Wear": true,
      "x": 193,
      "y": 334,
      "z": 71,
      "AxisXCounts": 193,
      "AxisYCounts": 334,
      "AxisZCounts": 71
    },
    {
      "TimestampUTC": "2020-03-24T00:31:00Z",
      "TimestampSubjectTZ": "2020-03-23T20:31:00",
      "Calories": 0.0154335947775919,
      "HR": 0.0,
      "Lux": null,
      "Steps": 0.0,
      "Wear": true,
      "x": 30,
      "y": 23,
      "z": 0,
      "AxisXCounts": 30,
      "AxisYCounts": 23,
      "AxisZCounts": 0
    }
  ]
"""

# let's create a json object (which will be a python list in this case)
# using the json library
json_arr = json.loads(json_arry_str)
print(type(json_arr))
print(json_arr)

for arr_obj in json_arr:
    print(arr_obj["TimestampSubjectTZ"], ":", arr_obj["Calories"])
    print(type(arr_obj))
    print("****")

# let's read the actigraph data from file
infile = open("actigraph_data.json", "r")
json_arr = json.load(infile)
print(type(json_arr))
print(json_arr)

for arr_obj in json_arr:
    print(arr_obj["TimestampSubjectTZ"], ":", arr_obj["Calories"])
    print(type(arr_obj))
    print("****")


# now again with pandas!
json_df = pd.read_json("actigraph_data.json")
print(json_df)

# doesn't give us correct columns
# thor_df = pd.read_json("thor_itunes_search.json")
# print(thor_df)

json_obj = json.load(open("thor_itunes_search.json"))
print(json_obj)
results_arr = json_obj["results"]
for result_obj in results_arr:
  track_name = (result_obj["trackName"])
  # task: grab the milliseconds and convert it to minutes, then check your work
  track_time_millis = result_obj["trackTimeMillis"]
  track_time_mins = track_time_millis / 1000 / 60
  print(track_name, ":", track_time_mins)
  print("****")

# json is a nice format to structure data