#!/usr/bin/env python3
######## EXPLORE READ ##########
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

## display file to the screen - .read()
print(configfile.read())

## close file
configfile.close()

######## EXPLORE READLINES ##########
## re-create file object to explore new method
configfile = open("vlanconfig.cfg", "r")

## make a list of file lines - .readlines()
configlist = configfile.readlines()
print(configlist)

## Iterate thrhough configlist
for x in configlist:
    print(x.lstrip(),end="") # left strip = lstrip or rstrip is right strip
    print(x.strip())
    #print(x,end="")

## Always close your file
configfile.close()

