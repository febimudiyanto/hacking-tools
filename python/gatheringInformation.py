# Date: 22-11-2021

import sys
import requests
import socket
import json

# check argument if argument empty
if len(sys.argv) < 2:
    print("Usage: "+ sys.argv[0] + " <url>")
    sys.exit(1)

# get request to url and print header
req = requests.get("http://"+sys.argv[1])
print("\n"+str(req.headers))

# get ip address
gethostby_ = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of "+sys.argv[1]+" is: "+gethostby_ + "\n")

# check Geolocation of IP address with ipinfo.io


req_ipinfo = requests.get("https://ipinfo.io/"+gethostby_+"/json")
resp_ = json.loads(req_ipinfo.text)

print("Location: "+resp_["loc"])
print("Region: "+resp_["region"])
print("City: "+resp_["city"])
print("Country: "+resp_["country"])
