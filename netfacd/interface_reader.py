#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

def getMacAddress(address):
    return(netifaces.ifaddresses(address)[netifaces.AF_LINK][0]['addr'])

def getIpAddress(address):
    return(netifaces.ifaddresses(address)[netifaces.AF_INET][0]['addr'])

for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    try: # This is a new line, you also need to indent the code below this line by 4 whitespaces
    #    print(netifaces.ifaddresses(i))
    #    print(netifaces.ifaddresses(i)[netifaces.AF_LINK])
       #print('MAC: ', end='') # This print statement will always print MAC without an end of line
       print('MAC: ', getMacAddress(i)) # This print statement will always print MAC without an end of line
       #print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
       #print('IP: ', end='')  # This print statement will always print IP without an end of line
       print('IP: ', getIpAddress(i))  # This print statement will always print IP without an end of line
       #print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
    except:  # This is a new line
       print('Could not collect adapter information') # Print an error message

