# irishrail.py
Python script that retrieves train details for provided departure and destination stations using the Irish Rail Realtime API (http://api.irishrail.ie/realtime/)

## Usage
The script takes 3 positional parameters in the following order:
1. The departure station name.
1. The time range for the query in minutes.
1. A list of destination stations for trains from the specified departure station.

### Optional Arguments
It also takes the following optional arguments:
1. **-h**, prints help information for the script.
1. **--ifttt**, indicates an IFTTT webhook url to post web requests to with script output passed as 'value1'


### Examples
`irishrail.py Portarlington 60 "Dublin Heuston" "Grand Canal Dock" "Portlaoise"`

`irishrail.py --ifttt "http://www.ifttt.com/my/webhook/url Maynooth 90 "Dublin Connolly"`
