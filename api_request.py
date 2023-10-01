from typing import NamedTuple
from enum import Enum
from datetime import datetime
from location import Coordinates

degrees_Celsius = int # type alias

class WeatherType(Enum):
    RAIN = 'Rain'
    CLEAR = 'Clear'
    SNOW = 'Snow'
    CLOUDY = 'Cloudy'
    FOGGY = 'Foggy'
    STORM = 'Storm'

class Weather(NamedTuple):
    temperature: degrees_Celsius
    weather_type: WeatherType 
    sunrise: datetime
    sunset: datetime 
    city: str

def get_local_weather(coordinates: Coordinates) -> Weather:
    '''request local weather by coordinates'''
    return Weather(
        temperature = 25,
        weather_type = WeatherType .CLEAR,
        sunrise = datetime.fromisoformat('2023-10-01 12:00:00'),
        sunset = datetime.fromisoformat('2023-10-01 12:00:00'),
        city = 'Amsterdam'
    )