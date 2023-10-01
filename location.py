from typing import NamedTuple

class Coordinates(NamedTuple):
    latitude: float
    longitude: float

def get_location() -> Coordinates:
    '''Returns current location via API call'''
    return Coordinates(latitude = 0, longitude = 0)