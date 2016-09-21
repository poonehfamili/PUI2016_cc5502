from __future__ import print_function
import json, urllib2, sys
from sys import argv

script, key, bus_line = argv

if not len(sys.argv) == 3:
    print("Invalid input, try again with your API key and a valid 3-digit bus line number.")

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + "&VehicleMonitoringDetailLevel=calls&LineRef="+bus_line
resp = urllib2.urlopen(url)
data = json.load(resp)

bus =  data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
no_of_buses = len(bus)
print('No of active buses: %d' %no_of_buses)

for i in range(no_of_buses):
    lat = bus[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    lng = bus[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print('Bus %d is at latitude %r and longitude %r' %(i, lat, lng))
