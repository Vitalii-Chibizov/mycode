#!/usr/bin/env python3
# lets run it more

bool = True
while bool:
# run it until I say stop
    hostname = input("What value should we set for hostname? ")
    if hostname.lower() == "mtg":
        print("The hostname was found to be mtg")
        print("hostname matches expected config")
    end = input("Type N if you want to exit code ")
    if end.upper() == "N":
        bool=false
        print("Exiting the script")
