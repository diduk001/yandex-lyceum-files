import sys
from io import BytesIO
from pprint import *

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

toponym_longitude, toponym_lattitude, toponym_delta = choose_size_geocoder(json_response_toponym)

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

pprint(organization)

# Получаем координаты ответа.
point_longitude, point_lattitude, point_delta = choose_size_search_api(organization)
org_point = f"{point_longitude},{point_lattitude}"

delta = str(2 * max(abs(point_longitude - float(toponym_longitude)), abs(point_lattitude -
                                                                         float(toponym_lattitude))))

# Собираем параметры для запроса к StaticMapsAPI:
map_params = {
    # позиционируем карту центром на наш исходный адрес
    "ll": f"{toponym_longitude},{toponym_lattitude}",
    "spn": ",".join([delta, delta]),
    "l": "map",
    # добавим точку, чтобы указать найденную аптеку
    "pt": '~'.join([f"{org_point},pm2dgl", f"{toponym_longitude},{toponym_lattitude},org"])
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
# ... и выполняем запрос
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(response.content)).show()
