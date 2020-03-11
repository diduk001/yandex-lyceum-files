import sys
from io import BytesIO
from math import sqrt

import requests
from PIL import Image
from choose_size import *

toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response_toponym = requests.get(geocoder_api_server, params=geocoder_params)

if not response_toponym:
    print("toponym_error")
    print(response_toponym.status_code)
    print(response_toponym.content)
    exit(-1)

# Преобразуем ответ в json-объект
json_response_toponym = response_toponym.json()

toponym_longitude, toponym_lattitude, toponym_delta = map(float,
                                                          choose_size_geocoder(
                                                              json_response_toponym))

search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

address_ll = f"{toponym_longitude},{toponym_lattitude}"

search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": address_ll,
    "type": "biz"
}

response = requests.get(search_api_server, params=search_params)
if not response:
    print(response.status_code)
    print(response.content)
    exit(-1)

json_response = response.json()

# Получаем первую найденную организацию.
organization = json_response["features"][0]
# Название организации.
org_name = organization["properties"]["CompanyMetaData"]["name"]
# Адрес организации.
org_address = organization["properties"]["CompanyMetaData"]["address"]
# Часы работы
org_hours = organization["properties"]["CompanyMetaData"]["Hours"]["text"]

# Получаем координаты ответа.
org_longitude, org_lattitude, org_delta = choose_size_search_api(organization)
org_coords = f"{org_longitude},{org_lattitude}"

delta = str(2 * max(abs(org_longitude - float(toponym_longitude)), abs(org_lattitude -
                                                                       float(toponym_lattitude))))

# Собираем параметры для запроса к StaticMapsAPI:
map_params = {
    # позиционируем карту центром на наш исходный адрес
    "ll": f"{toponym_longitude},{toponym_lattitude}",
    "spn": ",".join([delta, delta]),
    "l": "map",
    # добавим точку, чтобы указать найденную аптеку
    "pt": '~'.join([f"{org_coords},pm2dgl", f"{toponym_longitude},{toponym_lattitude},org"])
}

distance = sqrt((toponym_longitude - org_longitude) ** 2 + (toponym_lattitude - org_lattitude)
                ** 2)
CONST_METERS_IN_DEGREE = float(pow(10, 5)) * 0.5

# Формирование сниппета
snippet = [org_name, org_address, org_hours, int(CONST_METERS_IN_DEGREE * distance)]
snippet = list(map(str, snippet))
snippet[3] += " м"

# Печать сниппетов1
print('\n'.join(snippet))

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(response.content)).show()
