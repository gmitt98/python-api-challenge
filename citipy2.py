# Apr. 11. 2023. This is a customized improvement of the citipy module.
# New additions are commented in.
# The goal of this was to do two things:
#   1. add coordinates to the city object as well as the ability to return those coordinates with a method call
#   2. add a lookup function that allows the user to input a city name in string form and receive the coordinates in tuple form
# Combining these features means that now a user can take a set of coordinates, get the closest city, and get the true coordinates for that city
# This should allow other computations to occur and this module may be extended in the future
# I will attempt to add this to the original project, or if not, I will publish this as it's own open source project
# Go Ducks!

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
        return(self.city_long, self.city_lat)


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
    # NEW: added pushing in the city coordinates to the city object
    for city in cities:
        city_coordinate_key = (float(city[2]), float(city[3]))
        _world_cities_kdtree.add(city_coordinate_key)
        c = City(city[1], city[0], city[2], city[3])
        WORLD_CITIES_DICT[city_coordinate_key] = c


def nearest_city(latitude, longitude):
    nearest_city_coordinate = _world_cities_kdtree.search_nn((latitude, longitude, ))
    return WORLD_CITIES_DICT[nearest_city_coordinate[0].data]

# NEW: function with ability to return coordinates if given a city name
def get_coordinates(city_name):
    for coordinate_key, city in WORLD_CITIES_DICT.items():
        if city.city_name == city_name:
            return city.get_coordinates()