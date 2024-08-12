# Oct 12 Notes

# JSON = javascript object notation
# API = application programming interface
#   a set of functions that a programmer / organization exposes for other programmers / organizations to use
#   without needing to know how the functions are implemented
#   ex: Python math module exposes an API that we use: pow(), tan(), sin()
#   web API = an API that you access via the web
#       use cases: GET DATA, send data & request computational result, send data to update a resource (database)...

# Diagram how to request data from a web API
# client = webbrowser, programmer via command line, program via python script...
# server = listening for client requests
# we make a HTTPS GET request (url) and it goes through API to go to server which returns JSON response (dictionaires / lists)

# ser.index.name
# ser.name

import requests # a library for making HTTP requests
import json
import random

# using https://opentdb.com/api_config.php
url = "https://opentdb.com/api.php?amount=5&category=28&difficulty=hard"

response = requests.get(url=url)
print(response.text)
print()

json_object = json.loads(response.text) # .loads for strings

# task: extract and print the questions...
# challenge: for multiple choice questions, shuffle and print the possible answers
results_arr = json_object["results"]
for result_obj in results_arr:
    question = requests.utils.unquote(result_obj["question"])
    print(question)
    if result_obj["type"] == "multiple":
        # build a list of of the possible answers
        answers = [result_obj["correct_answer"]] + result_obj["incorrect_answers"]
        random.shuffle(answers) # so the correct answer isn't always the first option
        for answer in answers:
            print("\t" + requests.utils.unquote(answer))
    print("****")

# using https://opentdb.com/api.php?amount=10&category=16&difficulty=easy
# https: = protocol ("s" = request is secure and encrypted)
# //opentdb.com/ = domain name
# api.php? = path to endpoint
# ? = ends path and starts query string (or arguments/parameters), which is everything after the "?"
#   client specifies what they want
#   & separated list of key value pairs (key = amount and value = 10, key = category and value = 16, key = difficulty and value = easy)




