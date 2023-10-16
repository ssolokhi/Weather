from typing import NamedTuple
from exceptions import CannotFetchCoordinates
from geocoder import ip

class Coordinates(NamedTuple):
    latitude: float
    longitude: float

def get_device_location() -> Coordinates:
    '''Returns current device location via API call'''
    device_GPS_coordinates = ip('me')
    if device_GPS_coordinates is not None:
        device_latitude, device_longitude = device_GPS_coordinates.latlng
        return  Coordinates(latitude = device_latitude, longitude = device_longitude)
    else:
        raise CannotFetchCoordinates