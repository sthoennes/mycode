#!/usr/bin/env python3
import ipaddress
ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# a provided string will test true
if ipchk == "192.168.70.1":
    print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
elif ipchk:
    try: 
        ipaddress.ip_address(ipchk) 
        print("Looks like the IP address was set: " + ipchk) # indented under if
    except:
        print("Not a valid IP address.")
else: # data not provided
   print("Nothing entered.")
