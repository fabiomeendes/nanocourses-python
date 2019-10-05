from pygeocoder import Geocoder

# address = "Avenida Paulista, 100 Sao Paulo"
# result = Geocoder("AIzaSyAhgA6CciTBT3sOz0W0bE4HHPuGVq1AF7U").geocode(address)
# print(result)

result = Geocoder('AIzaSyAhgA6CciTBT3sOz0W0bE4HHPuGVq1AF7U').reverse_geocode(-23.5703022, -46.6451267)
print(result)
