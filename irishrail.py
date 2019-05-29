#!/usr/bin/python3.6

import requests
import sys

from xml.etree import ElementTree

if len(sys.argv) < 3:
    print("ERROR: No enough parameters provided")
    print("usage: irishrail.py <departure station> <destination station> [... <departure station N>]")
    exit(1)

station = sys.argv[1]

dest_stations = sys.argv[2:]

url = "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByNameXML?StationDesc=" + station

response = requests.get(url)

tree = ElementTree.fromstring(response.content)

msg = ""

for train_data in tree:
    dest = train_data.find('{http://api.irishrail.ie/realtime/}Destination').text
    late = train_data.find('{http://api.irishrail.ie/realtime/}Late').text
    if dest in dest_stations:
        msg = msg + train_data.find('{http://api.irishrail.ie/realtime/}Scharrival').text + " to " + dest
        if late == "0":
            msg = msg + " is on time"
        else:
            msg = msg + " is " + late + " minutes late.\n"

print(msg)




