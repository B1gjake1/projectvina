import urllib.request
import json
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyBgx5MH1r1ay3X5h-2kx8JhMDkGHBPXVB4'
geocode = 'https://www.googleapis.com/geolocation/v1/geolocate?key={}'.format(api_key)

origin = input('locations?: ').replace(' ', '+')
destination = input('where do you want to go?:').replace(' ', '+')


nav_request = 'origin={}&destination={}&key={}&mode=walking'.format(origin,destination,api_key)

request = endpoint + nav_request
response = urllib.request.urlopen(request).read()
directions = json.loads(response)



print(request)

