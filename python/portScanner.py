date = 23-11-2021

import nmap #pip3 install python-nmap
import sys

target = str(sys.argv[1])
ports = [21,22,80,139,443,8080]

scanner = nmap.PortScanner()

print("\nScanning",target,"for ports 21,22,80,139,443,8080...\n")

for port in ports:
    portscan = scanner.scan(target,str(port))
    print("Port",port,"is",portscan['scan'][target]['tcp'][port]['state'])

print("\nHost",target,"is",portscan['scan'][target]['status']['state'])
