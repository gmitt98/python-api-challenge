# updated original citipy module to have coordinates as part of the object. new code is mentioned in comments.
# also included a function to give coordinates for a given city name
# this function takes the first city by the name that it finds in the csv data

import csv
import kdtree
import os


class City:
    '''
    City wraps up the info about a city, including its name, coordinates,
    and belonging country.
    '''
    # NEW: adding the actual coordinates to the object
    def __init__(self, city_name, country_code, city_lat, city_long):
        self.city_name = city_name
        self.country_code = country_code
        self.city_lat = city_lat
        self.city_long = city_long
    # NEW: ability to return coordinates
    def get_coordinates(self):
        return(self.city_lat, self.city_long)


# load the city data up
_current_dir, _current_filename = os.path.split(__file__)
_world_cities_csv_path = os.path.join(_current_dir, 'worldcities.csv')
_world_cities_kdtree = kdtree.create(dimensions=2)
WORLD_CITIES_DICT = {}

with open(_world_cities_csv_path, 'r') as csv_file:
    cities = csv.reader(csv_file)

    # discard the headers
    cities.__next__()

    # populate geo points into kdtree
    for city in cities:
        city_coordinate_key = (float(city[2]), float(city[3]))
        _world_cities_kdtree.add(city_coordinate_key)
        c = City(city[1], city[0], city[2], city[3])
        WORLD_CITIES_DICT[city_coordinate_key] = c


def nearest_city(latitude, longitude):
    nearest_city_coordinate = _world_cities_kdtree.search_nn((latitude, longitude, ))
    return WORLD_CITIES_DICT[nearest_city_coordinate[0].data]

# NEW: ability to return coordinates from a name input - takes the first name it finds
# Use caution in case of duplicates
def get_coordinates(city_name):
    for coordinate_key, city in WORLD_CITIES_DICT.items():
        if city.city_name == city_name:
            return city.get_coordinates()
