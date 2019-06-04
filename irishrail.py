#!/usr/bin/python

import requests
import sys
import argparse

from xml.etree import ElementTree

parser = argparse.ArgumentParser(description="Retrieve train details from Irish Rail realtime API.")
parser.add_argument('dept_station', metavar='<dept station>', type=str, help="the departure station.")
parser.add_argument('time_range', metavar='<num of mins>', type=int, help="the time range of the query in minutes.")
parser.add_argument('dest_stations', metavar='<dest station>', type=str, nargs='+', help="list of destination stations")
parser.add_argument('--ifttt', type=str, help="IFTTT webhook url")

args=parser.parse_args()

dept_station = args.dept_station

time_range = args.time_range

dest_stations = args.dest_stations

ifttt_url = args.ifttt

url = "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByNameXML_withNumMins?StationDesc=" + dept_station \
      + "&NumMins=" + str(time_range)

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

if ifttt_url is not None:
	requests.post(ifttt_url, json={"value1": msg})
