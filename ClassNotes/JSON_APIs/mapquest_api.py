
import requests
import json

api_key = "yzaGHHCwd14UflR663zZj2xOEA5L4861"

url = "http://www.mapquestapi.com/directions/v2/route"

# we need a key, a from, and a to

url += "?key=" + api_key
url += "&from=spokane"
url += "&to=seattle"

print(url)


# task: extract the distance and duration from the response
response = requests.get(url=url)
json_object = json.loads(response.text)

route_obj = json_object["route"]
distance = route_obj["distance"]
print(distance)

formatted_time = route_obj["formattedTime"]
print(formatted_time)
