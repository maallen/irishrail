# irishrail.py
Python script that retrieves train details for provided departure and destination stations using the Irish Rail Realtime API (http://api.irishrail.ie/realtime/)

## Usage
The script takes 3 parameters in the following order:
1. The departure station name
1. The time range for the query
1. A list of destination stations for trains from the specified departure station.

### Example
`irishrail.py Portarlington 60 "Dublin Heuston" "Grand Canal Dock" "Portlaoise"`
