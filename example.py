# example
# https://nominatim.openstreetmap.org/search?q=lima,peru&format=json

import requests
import json

def get_coordinates(city):
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    headers = {
        'User-Agent': 'Testing App'
    }
    response = requests.get(url, headers=headers)


    if response.status_code != 200:
        return None

    try:
        data = response.json()
        return {
            'lat': data[0]['lat'], 
            'lon': data[0]['lon']
            }
    except Exception as e:
        print(e)
        return None

def get_distance(origin, destination):
    try:
        originX = origin['lat']
        originY = origin['lon']

        destinationX = destination['lat']
        destinationY = destination['lon']

        distance = ((float(destinationX) - float(originX))**2 + (float(destinationY) - float(originY))**2)**0.5

        #round 2 decimal places
        distance = round(distance, 2)

        return distance
    except:
        return None