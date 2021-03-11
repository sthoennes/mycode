#!/usr/bin/env python3
#CALCULATOR
# take input from user input()
# if/elif/else <- if then else
#functions
#while loops <- repeat sections until a certain criteria is met
#define constants and variable
valid_ops

# can add (math) or concatenate

def addition(a,b):
    addemup= a + b
    #print(addemup)
    return addemup #return sends you to next code where you left off I think
def subtraction(a,b):
    #subtractem= a - b
    return (a - b)

def multem(a,b):
    multemup= a * b
    return multemup

def divideem(a,b):
    divyemup= b/a
    return divyemup

def expon(a,b):
    exponemup= a**b
    return exponemup


def calc(): #input the number in a and c and the operator in b
    while True:
        try:
            x = float(input("Enter first number: "))
            #x = decimal(input("Enter first number: "))
            break
        except:
            print("Please re-enter a number: ")
    while True:
        try:
            operator = input("Enter operator: ")
            if operator == 






a=b=0.0
operator=""
x=y=0.0
#while True:
#    round += 1

x=input("Enter first number x: ")

#    if x 

y=input("Enter second number y: ")

operator=input("Enter operator to use (+, -, /, *, or ^) or 'Q' to quit: ")

print(int(x),int(y),operator)


if operator == "+":
    addition(x,y)
    print("operator: ",operator)
    print(f"{x} and {y} added is {addition(x,y)}")
    
elif operator == "-":
    subtraction(x,y)
elif operator == "/":
    if y == 0:
        print("cant deviide by 0")
    elif y !=0:
        divideem(x,y)
elif operator == "*":
    multem(x,y)
elif operator == "^":
    expon(x,y)
elif operator == "Q":
    print("Quitting routine")





#num1="Python"
#num2=" is cool"
#addition(num1,num2)
#num3=3470
#num4=0
#addition(num3,num4)
#num5=23456789
#num6=3255523
#addition(num5,num6)

#print(f"The total of {num5} and {num6} is {addition(num5,num6)}")
#print(f"{x} and {y} added is {addition(x,y)}")
