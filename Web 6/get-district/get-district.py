import sys

import requests
from choose_size import *


def get_district(geo_object_json):
    address = geo_object_json["metaDataProperty"]["GeocoderMetaData"]["Address"]
    components = address["Components"]
    for component in components:
        if component["kind"] == "district":
            return component["name"]
    return None


toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_toponym_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response_toponym = requests.get(geocoder_api_server, params=geocoder_toponym_params)

if not response_toponym:
    print("toponym_error")
    print(response_toponym.status_code)
    print(response_toponym.content)
    exit(-1)

# Преобразуем ответ в json-объект
json_response_toponym = response_toponym.json()

toponym_longitude, toponym_lattitude, _ = map(float,
                                              choose_size_geocoder(
                                                  json_response_toponym))

geocoder_district_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": f"{toponym_longitude},{toponym_lattitude}",
    "kind": "district",
    "format": "json"}

response_district = requests.get(geocoder_api_server, params=geocoder_district_params)

if not response_district:
    print("district error")
    print(response_district.status_code)
    print(response_district.content)
    exit(-1)

# Преобразуем ответ в json-объект
json_response_toponym = response_toponym.json()

geo_object = json_response_toponym["response"]["GeoObjectCollection"]["featureMember"][0][
    "GeoObject"]
district = get_district(geo_object)

# Геокодер не всегда находит Район, но точно находит район по адресу Ленинские горы, 1

if district is None:
    print("Района не найдено")
else:
    print(district)