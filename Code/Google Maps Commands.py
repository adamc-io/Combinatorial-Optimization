import googlemaps
from datetime import datetime


# Set up the API key for google maps
# https://developers.google.com/maps/documentation


# Below is a list of common google maps commands found in the googlemaps documentation
# https://googlemaps.github.io/google-maps-services-python/docs/#


# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

# Find a place
find_place_result = gmaps.find_place('Google Shoes!',
                                     'textquery',
                                     fields=['name', 'geometry'])

# Nearby search
nearby_result = gmaps.places_nearby(location='Sydney Town Hall',
                                    radius=500,
                                    open_now=False,
                                    type='store')

# Text search
text_search_result = gmaps.places('restaurant')

# Radar search
radar_search_result = gmaps.places_radar(location=(51.5034070, -0.1275920),
                                         radius=500,
                                         keyword='pizza')

# Distance matrix
origin = (40.6655101, -73.89188969999998)
destination = (40.6905615, -73.9976592)
dm = gmaps.distance_matrix(origin, destination)

# Elevation
elevations_result = gmaps.elevation((40.714728, -73.998672))

# Elevation along a path
path = [(40.737102, -73.990318),
        (40.749825, -73.987963),
        (40.752946, -73.987384),
        (40.755823, -73.986397)]
