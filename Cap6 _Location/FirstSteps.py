from pygeocoder import Geocoder

address = '1222, Lins de Vasconcelos, Sao Paulo, SP'
print(Geocoder('AIzaSyAhgA6CciTBT3sOz0W0bE4HHPuGVq1AF7U').geocode(address).coordinates)
# return lat lng
