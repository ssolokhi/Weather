# no realization, only logical blocks to be executed

from location import get_location
from api_request import get_local_weather
from display_weather import print_weather

def weather():
    location = get_location()
    weather = get_local_weather(location)
    print(print_weather(weather))

if __name__ == '__main__':
    weather()