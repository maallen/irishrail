#!/usr/bin/python3.6

import requests
import sys

from xml.etree import ElementTree

if len(sys.argv) < 2:
    print("ERROR: No station name parameter passed to script")
    exit(1)

station = sys.argv[1]

url = "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByNameXML?StationDesc=" + station

response = requests.get(url)

tree = ElementTree.fromstring(response.content)

msg = ""

for train_data in tree:
    dest = train_data.find('{http://api.irishrail.ie/realtime/}Destination').text
    late = train_data.find('{http://api.irishrail.ie/realtime/}Late').text
    if dest == "Dublin Heuston" or dest == "Grand Canal Dock":
        msg = msg + train_data.find('{http://api.irishrail.ie/realtime/}Scharrival').text + " to " + dest
        if late == "0":
            msg = msg + " is on time"
        else:
            msg = msg + " is " + late + " minutes late.\n"

print(msg)




