#!/usr/bin/env python3
## create file object in "r"ead mode
# next line is for challenge4 in the lab 27
choice=input("enter file")

with open("vlanconfig.cfg", "r") as configfile:
#with open(choice, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
  #  len(configlist) #counts lines in configlist
    
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print("num of lines in configlist",len(configlist)) #does the counting of configlist here



