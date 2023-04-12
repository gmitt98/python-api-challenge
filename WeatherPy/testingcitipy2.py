import citipy2
mycoord = citipy2.get_coordinates('eugene')
print(mycoord)
mycity = citipy2.nearest_city(44, -123.1)
print(mycity)
print(mycity.city_name, mycity.country_code, mycity.city_lat, mycity.city_long)
