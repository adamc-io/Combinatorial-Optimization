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

