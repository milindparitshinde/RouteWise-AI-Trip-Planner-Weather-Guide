import requests
from geopy.distance import geodesic
from langchain.tools import tool

ORS_API_KEY = "ORS API KEY HERE"
ORS_DIRECTIONS_URL = "https://api.openrouteservice.org/v2/directions/driving-car"
ORS_GEOCODE_URL = "https://api.openrouteservice.org/geocode/reverse"

# Step 1: Get route coordinates
def get_route_coordinates(start, end):

    headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    }

    call = requests.get(f'https://api.openrouteservice.org/v2/directions/driving-car?api_key={ORS_API_KEY}&start={start}&end={end}', headers=headers)

    print(call.status_code, '\n', call.reason)
    print(call.text)

    return call.json()


# Step 2: Sample route coords at roughly every N kilometers
def sample_route_points(coords, interval_km=20):
    sampled = [coords[0]]
    prev_point = coords[0]

    for point in coords[1:]:
        dist = geodesic((prev_point[1], prev_point[0]), (point[1], point[0])).km
        if dist >= interval_km:
            sampled.append(point)
            prev_point = point
    return sampled


# Step 3: Reverse geocode points
def reverse_geocode(coord):
    params = {
        "api_key": ORS_API_KEY,
        "point.lon": coord[0],
        "point.lat": coord[1]
    }
    response = requests.get(ORS_GEOCODE_URL, params=params)
    response.raise_for_status()
    data = response.json()

    features = data.get('features', [])
    if features:
        # Return place name or city (customize as needed)
        return features[0]['properties'].get('name') or features[0]['properties'].get('county')
    return None

#TOOLS 1: Get key places along route
@tool
def get_key_places(start: str, end: str):
    """Get key places along the route from start to end."""
    data = get_route_coordinates(start, end)

    main_route_points = sample_route_points(data['features'][0]['geometry']['coordinates'], interval_km=50)

    key_places = []

    for coord in main_route_points:
        place = reverse_geocode(coord)
        if place and place not in key_places:
            key_places.append(place)

    return key_places

# Tool 2: Get weather forecast for location
# def get_weather(location, datetime):
#     # Call weather API here
#     return weather_info
@tool
def get_weather(location: str, date: str):
    """Get weather forecast for a given location and date."""
    WEATHER_API_KEY='WEATHER API KEY HERE'
    url = f"http://api.weatherapi.com/v1/forecast.json"

    headers = {
        'key': WEATHER_API_KEY,
        'Content-Type': 'application/json'
    }

    body = {
        "q": location,
        "days": 1,
        "dt": date
    }

    response = requests.get(url, headers=headers, params=body)

    return response.json()

# # Tool 3: Analyze weather along route and suggest departure time & rest stops
# def analyze_weather(route, preferred_weather):
#     # Logic to find best time to leave or suggest stops
#     return suggestion_summary