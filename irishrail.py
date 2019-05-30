#!/usr/bin/python

import requests
import sys

from xml.etree import ElementTree

if len(sys.argv) < 4:
    print("ERROR: Not enough parameters provided")
    print("usage: irishrail.py <departure station> <time range in minutes> <destination station> "
          "[... <departure station N>]")
    exit(1)

station = sys.argv[1]

time_range = sys.argv[2]

dest_stations = sys.argv[3:]

url = "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByNameXML?StationDesc=" + station \
      + "&NumMins=" + time_range

response = requests.get(url)

tree = ElementTree.fromstring(response.content)

msg = ""

for train_data in tree:
    dest = train_data.find('{http://api.irishrail.ie/realtime/}Destination').text
    late = train_data.find('{http://api.irishrail.ie/realtime/}Late').text
    if dest in dest_stations:
        msg = msg + train_data.find('{http://api.irishrail.ie/realtime/}Scharrival').text + " to " + dest
        if late == "0":
            msg = msg + " is on time.\n"
        else:
            msg = msg + " is " + late + " minute(s) late.\n"

print(msg.strip())
