#!/usr/bin/python3

import ipaddress

#ipchk = '192.168.0.1'
ipchk = input('Apply a IP address: ')

try:
    ipaddress.ip_address(ipchk)
    if ipchk == '192.168.70.1':
        print("looks like the IP address was set: " + ipchk + "This is not recommanded.")
    else:
        print("looks like the IP address was set: " + ipchk )
#    else:
#        print("You did not provide input, dummy.")

except:
    print("That is not appear to be a valid IP address.")
