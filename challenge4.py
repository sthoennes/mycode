#!/usr/bin/python3
totalqs = 1
answer = " "
countryvotes = 0
cityvotes = 0

#while totalqs < 6: #do until no answer or 

answer = input('Q1:Do you like the smell of manure?').lower()
if answer == 'y':
    countryvotes += 1
else:
    cityvotes+= 1
#    totalqs += 1    
answer = input('Q2:Would you rather own a hobby farm than a city lot?').lower()
if answer == 'y':
    countryvotes += 1
else:
    cityvotes+= 1
#    totalqs += 1    
answer = input('Q3:Do you have serious serial allergies?').lower()
if answer == 'y':
    cityvotes += 1
else:
    countryvotes+= 1
#    totalqs += 1    
answer = input('Q4:Would you like farm animals as pets?').lower()
if answer == 'y':
    countryvotes += 1
else:
    cityvotes+= 1
#    totalqs += 1    
answer = input('Q5:Is your style of clothing more jeans and t-shirts than dress-shirts and slacks?').lower()
if answer == 'y':
    countryvotes += 1
else:
    cityvotes += 1
#    totalqs += 1    
if cityvotes > countryvotes:
    print("You would prefer city living")
else:
    print("You would prefer country living")

    
