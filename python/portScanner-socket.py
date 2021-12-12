# Date = 12 - 12 - 2021

import socket
import sys


# check argument if argument empty
if (len(sys.argv) < 2) or (sys.argv[1] == ('-h')):
    print("Usage: "+ sys.argv[0] + " <ip target> <portrange> <option>")
    print("example:\n\t\t"+ sys.argv[0] +" 192.168.0.1 1000-2000\n\t\t"+ sys.argv[0] +" 192.168.0.1 1000-2000 -O")
    
    print("OPTIONS:\n\t-O   --open  : just show open port")
    sys.exit(1)
    
if (len(sys.argv) <= 3):
  flag = ""
else:
  flag = str(sys.argv[3])

target = str(sys.argv[1])
portRange = str(sys.argv[2])

lowPort = int(portRange.split("-")[0])
highPort = int(portRange.split("-")[1])

if highPort-lowPort > 100:
  flag = "-O"

for port in range(lowPort,highPort):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  status = s.connect_ex((target,port))
  if (status == 0):
    print("*** Port",port,"- OPEN ***")
  elif (flag != "-O") and (flag != "--open"):
    print("Port",port,"- CLOSED")
s.close()
