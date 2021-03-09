#!/usr/bin/env python3

# create list with IP port and state
my_list = [ "192.168.0.5", 5060, "UP" ]

#print 1st item in list
print("The first item in the list (IP): " + my_list[0] )

#print second item in list
print("The second item in the list (port): " + str(my_list[1]) )

#print last item in list
print("The last item in the list (state): " + my_list[2] )

# create new list with 6 items
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print("When I",new_list[-1]," into IP addresses",new_list[3],"or",new_list[4],"I am unable to ping ports",new_list[0],",",new_list[1],",",new_list[2])

print(f"When I [new_list[5]} into IP addresses [new_list[3]} or [new_list[4]} I am unable to ping port {new_list[0], {new_list[1]})


