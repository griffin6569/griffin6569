import requests
import googlemaps

API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"

def get_route(start, destination):
    gmaps = googlemaps.Client(key=API_KEY)
    directions = gmaps.directions(start, destination, mode="driving")
    return directions
