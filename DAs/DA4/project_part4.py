'''
Colleen Lemak
Professor Sprint
CPSC 222
21 October 2021

Description: I chose to look into the Harry Potter API (documentation link: https://hp-api.herokuapp.com/). 
This API gives the user access to information on Harry Potter characters.  You can parse to get specific information on
all characters, all characters who are Hogwarts students during the book series, all characters who are Hogwarts 
staff during the book series, and all characters in a certain house.
'''

import requests
import json

# make url
harry_potter_url = "http://hp-api.herokuapp.com" + "/api/characters" 

# make request and load data into json object
response = requests.get(url=harry_potter_url)
json_object = json.loads(response.text)

# parse to get and store all name values from json object
characters_list = []
for idx in range(len(json_object)):
    route_object = json_object[idx]
    character_names = route_object["name"]
    characters_list.append(character_names)

# define pretty_print() function
def pretty_print(list):
    for value in list:
        print(value)

pretty_print(characters_list)
