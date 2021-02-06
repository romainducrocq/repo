#!/bin/python3

import sys #allows cmd line args
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate a host name to IPV4
else:
    print("Invalid amount of arguments.")
    print("Syntax ./scanner.py <pi>")
    sys.exit()

#Add a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) #is a float
        result = s.connect_ex((target, port)) #returns error indicator
        print("Checking port {}".format(port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExciting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
    sys.exit()

#ex :
# ./scanner.py liveplug_wi-fi_7562.home
# ./scanner.py 192.168.1.32
# Port 80 is open
