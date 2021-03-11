#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # This is much easier than using the urllib.request library

    print(r.json()) # has spaces for easier readability
    r = r.json() # assigns class to r
    #print(r.text) # takes out extra spaces between dict and list entries
    #print(type(r)) # print type of class - in this case it's Python list
main()

