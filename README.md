# python-api-challenge
## bootcamp module 6 challenge

The main folder for this project is WeatherPy, which contains the two notebooks used. API keys are not tracked on Github.
The folder output_data contains the city data called from the weather API and the resulting charts requested.

### Note:
The WeatherPy notebook used the citipy module. However, I had difficulty with this module and also wanted additional features that it did not have.
I copied it and made a citipy2 module that is in the main project folder. My notebook uses this module instead.
I also copied the unit testing file for the original module and updated it to demonstrate that this works.
The module is documented and there is a longer explanation in the note for my notebook code.

Caution: the .get_coordinates attribute will only grab the first value in the list for a city name. There are cities that share names.

### Example of citipy2 in use:

import citipy2

mycoord = citipy2.get_coordinates('eugene')

print(mycoord)

> ('44.0522222', '-123.0855556')

mycity = citipy2.nearest_city(44, -123.1)

print(mycity)

> <citipy2.City object at 0x1092c9690>

print(mycity.city_name, mycity.country_code, mycity.city_lat, mycity.city_long)

> eugene us 44.0522222 -123.0855556
