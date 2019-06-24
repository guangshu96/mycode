#!/usr/bin/pyton3

my_list = ["192.168.0.5", 5080, "UP"]

print("The first item is the List (IP): " + my_list[0])

print("The second item is the list (port): " + str(my_list[1]))

print("The second item is the list (state): " + my_list[2])

new_list = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

#print("When I %s into IP addresses %s or %s I am unable to ping ports %s, %s, or %s", new_list[5], new_list[3], new_list[4]), new_list[0], new_list[1], str(new_list[4]))


#print("When I %s into IP addresses %s or %s I am unable to ping ports %s, %s, or %s", new_list[5], new_list[3], new_list[4]), new_list[0], new_list[1], str(new_list[4]))
 

print(f"When I ssh into IP address {new_list[3] or {new_list[4] I am unable to ping ports {new_list[0]}, {new_list[1]}, {new_list[0]},")
