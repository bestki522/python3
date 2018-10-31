import socket
import sys
#import os

filename = input("Hello, please enter file name here > ")
try:
    infile = open(filename)
except EnvironmentError as e:
    print(e)
    sys.exit(1)

print("\nFile {} exists!".format(filename))
print("\nGetting IP addresses for hosts in your file")
print("\n")

for line in open(filename):
    hostname = line.strip()
    try:
        ip_address = socket.gethostbyname(hostname)
    except EnvironmentError as e:
	print("Couldn't find IP address for {}: {}".format(hostname, e))
	continue
    print("IP address for {0} is {1}.".format(hostname, ip_address))
else:
    print ("\nFinished the operation")
