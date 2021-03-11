#!/usr/bin/env python3
# imports always go at the top of your code
import requests

# Make a request to a web page, and print the response text
# resp below indicates what our response is back from server at given web address 
resp = requests.get("http://api.open-notify.org/astros.json")
print("If I reach site ok, response should be in the 200s: ",resp, resp.text)

# the data at http address is in json format and this turns it into a dict with 3 key:values pairs - Pythonic structures 
resp=resp.json()

#print(type(resp)) <- this shows that resp is a dictionary now because we took the json of the response vs text

# This prints number of astronauts, their names and the craft they're on
print(resp["number"])
for x in resp["people"]:
        print(f"{x['name']} is on the {x['craft']}")



