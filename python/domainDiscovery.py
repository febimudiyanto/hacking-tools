# date = 26-11-2021

import requests
import sys

if len(sys.argv) < 3:
    print("Usage: "+ sys.argv[0] + " <url>"+ " <wordlist>")
    sys.exit(1)

sub_list = open(sys.argv[2]).read()
subs = sub_list.splitlines()

for sub in subs:
    urlToCheck = f"http://{sub}.{sys.argv[1]}"

    try:
        r=requests.get(urlToCheck)
        status = r.status_code
    except requests.ConnectionError:
        pass

    else:
        print("Valid domain: ",urlToCheck,"   [",status,"]")
