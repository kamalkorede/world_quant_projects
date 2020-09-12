import requests

def fetch_ip_address():
    """Return a string of my IP address."""
    response = requests.get('https://api.ipify.org')
    
    return response.text


def locate_ip_address(ip_address):
    """Return latitude and longitude for a given IP address"""
    response = requests.get(f'http://ip-api.com/json/{ip_address}')
    data = response.json()
    
    return data['lat'], data['lon'], data['city'], data['regionName'], data['country']


def get_temperature(lat, lon):
    """Return current temperature for a location given the latitude and longitude."""
    url_base = 'https://api.met.no/weatherapi/locationforecast/2.0/compact'

    response = requests.get(url_base, params={'lat': lat, 'lon': lon})
    data = response.json()
    temperature = data['properties']['timeseries'][0]['data']['instant']['details']['air_temperature']
    
    return temperature


def convert_to_fahr(temp_C):
    return 9 / 5 * temp_C + 32


def greet(ip_address):
    # ip_address = fetch_ip_address()
    lat, lon, city, state, country = locate_ip_address(ip_address)
    temp_C = get_temperature(lat, lon)
    temp_F = convert_to_fahr(temp_C)
    
    return f"It's {temp_C} deg Celsius or {temp_F} deg F in {state}, {country}. "


if __name__=='__main__':
    import sys
    
    print(greet(sys.argv[1]))
