#!/usr/bin/env python3

# manipulate icecream list
icecream = ["flavors","salty"]
number=99

# append 99 to icecream list
#icecream.append(99)
icecream.append(number)

# Ask for user's name
name=input("Please type in your name: ")

# combine icecream in input for final statement 
print(icecream[2],icecream[0] + ", and",name,"chooses to be",icecream[1])

#F-string lets you get rid of extra apostrophes and commas
print(f"{icecream[2]} {icecream[0]}, and {name} chooses to be {icecream[1]}.")
#heroes={"Groot":{"Intelligence":"dumbest"
