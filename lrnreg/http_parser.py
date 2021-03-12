#!/usr/bin/env python3

import urllib.request
import re

while True:
    print("Enter URL to search or hit enter to quit?")
    url = input()
    #if url.lower() == "q" or str(url) == "":
    if str(url) == "" or str(url)[0:4] != "http":
        print("Aw, sorry you don't want to play. Exiting program.")
        break
    else:
        print("\nWhat phrase would you like to search for in URL, " + str(url) + "?")
        searchFor = input()
        searchMe = urllib.request.urlopen(url).read().decode("utf-8")
        if re.search(searchFor, searchMe):
            counter = len(re.findall(searchFor, searchMe, flags=re.IGNORECASE))
            print("\nWe found",counter,"matches for the phrase,'" + str(searchFor) + "', in URL!\n")
        else:
            #print("\nSorry, no matches for the phrase,'",str(searchFor),"', was found!")
            print("\nSorry, no matches for the phrase,'" + str(searchFor) + "', was found!\n")
