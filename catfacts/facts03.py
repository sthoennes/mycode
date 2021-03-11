#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests
import random

def main():
    """Run time code"""
    ## create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts')

    ## catfact is our iterable -- that just means it will take on the values found within
    ## r.json()["all"], one after the next-- which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary
    ## print the value associated with text"
    #print(r.url)
    #print(r.text)
    #print(r.status_code)
    #print(r.iter_lines)
    #print("")
    #print(r.raw)
    buildlist = []
    for catfact in r.json():
        buildlist.append(catfact.get("text"))
        #print(catfact.get("text"))  # the .get() method returns NONE if key not found
        #print(type(catfact.get("text")))
        #print(random.randint(0,100))
    print(random.choice(buildlist))
main()
