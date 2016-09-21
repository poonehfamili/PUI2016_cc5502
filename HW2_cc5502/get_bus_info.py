from __future__ import print_function
import json, urllib2, csv, sys
from sys import argv

script, key, bus_line, busline_csv = argv

if not len(sys.argv) == 4:
  print("Invalid input, Please enter right arguments")

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+ key+"&VehicleMonitoringDetailLevel=calls&LineRef="+bus_line
resp = urllib2.urlopen(url)
data = json.load(resp)

bus =  data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
no_of_buses = len(bus)

file_out = open(busline_csv, 'wt')
writer = csv.writer(file_out)
writer.writerow(('Latitude','Longitude','Stop Name','Stop Status'))

for i in range(no_of_buses):
    lat = bus[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    lng = bus[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    if bus[i]['MonitoredVehicleJourney']['OnwardCalls'] == '':
      stop_name == 'N/A'
      stop_stat == 'N/A'
    else:
      stop_name = bus[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
      stop_stat = bus[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
      row = [lat,lng,stop_name,stop_stat]
      writer.writerow(row)
file_out.close()

file_read = open(busline_csv, 'rt')
reader = csv.reader(file_read)
for row in reader:
  print(row)

