# no realization, only logical blocks to be executed

from location import get_device_location
from api_request import get_local_weather
from display_weather import format_weather
from exceptions import CannotFetchCoordinates, CannotFetchWeather

def weather():
    try:
        device_location = get_device_location()
    except CannotFetchCoordinates:
        print('Couldn\'t fetch user\'s coordinates')
        exit(1)

    try:
        weather = get_local_weather(device_location)
    except CannotFetchWeather:
        print('Couldn\'t fetch local weather')
        exit(1)
    
    print(format_weather(weather))

if __name__ == '__main__':
    weather()