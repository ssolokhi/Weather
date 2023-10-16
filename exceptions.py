class CannotFetchCoordinates(Exception):
    '''API couldn't fetch user's location coordinates'''
    pass

class CannotFetchWeather(Exception):
    '''API couldn't fetch user's local Weather'''
    pass