#!/usr/bin/env python3

def floater():

    x= float(input("How would you rank your day today on a scale of 1-10?"))
    if x == 10:
        print("Attaboy! Stay positive!")
    elif x >= 8:
        print("Sounds lovely! Keep on truckin'!")
    elif x >= 6:
        print("Chin up, buttercup!")                    
    elif x >= 4:            
        print("I recommend some hot chocolate and a hug, maybe...")               
    elif x >= 2:
        print("Dude, are you ok?")                   
    else:
        print("Geez!!! You might as well just go back to bed!")

floater()

def python_props(x,y):
    #x= "fun"
    #y= "useful"
    print(f"Python is {x} and {y}!")


#a=b=""
#a=input("Enter adjective number one, a:")
#b=input("Enter adjective number two, b:")
#python_props(yypa,b)
python_props("ch","yp")

# define a function that takes an arg
def spongebobber(stringomobop):

# code that randomly capitalized whatever sting is fed into it
    from random import choice
    print(''.join(choice((str.upper, str.lower))(c) for c in stringomobop))

spongebobber("Yikes, I am not getting this stuff!")
# to print as string



