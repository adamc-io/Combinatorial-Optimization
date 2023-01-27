# Libraries used: pandas, googlemaps, datetime
import googlemaps
from datetime import datetime
import pandas as pd
import os

# Set up the API key for google maps, in order to get an api key see directions in the Google Maps Commands.py file
with open('/Users/adamchoy/Desktop/Google Maps API Key/API_KEY.txt') as f:
    file_path_to_api_key = f.read()

# Read the API key from the file and start the google maps client
gmaps = googlemaps.Client(key=file_path_to_api_key)


# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Oakton, VA",
                                     "Washington, DC",
                                     mode="driving",
                                     optimize_waypoints=True,
                                     departure_time=now)

# the results of this are in a json format, so we need to normalize the json result
print(directions_result[0]['legs'][0]['distance']['text'])
print(directions_result[0]['legs'][0]['duration']['text'])


# Constraints for the optimization
'''
User inputs a list of pick up locations and drop off locations if no drop off location is specified, 
then the drop off location is assumed to be the warehouse and requires user to determine if the route needs to 
return to the ware house or if it can continue, 

User inputs the preferred date and time of the pick up and drop off, if no values are provided it assumes best possible 
time and date

User inputs the minimum truck size required for the job, if no value is provided it assumes any truck is possible 
and chooses the best route

User inputs the capacity of the load size, if no capacity is given the value is assume to be zero

User inputs the est. time of job for each location, if no value is given the value is assumed to be zero

No job can start before 8 AM and must end before 10 PM

'''

# Example of the user input

#  |PickUp Loc|DropOff Loc|Pref. Date|Pref. Time|Min.Truck Size|ReturntoWarehouse|Load Capacity|Time@PckUp|Time@DrpOff|
#  |----------|-----------|----------|----------|--------------|-----------------|-------------|----------|-----------|
#  |12 Main St|456 Main St|01/01/2020| 12:00 PM |  Box Truck   |        Yes      |      10     |    10    |    10     |
#  |12 Main St|456 Main St|   N/A    |    N/A   |  White Truck |         No      |      0      |    10    |    0      |

