import sys
from io import BytesIO

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

toponym_longitude, toponym_lattitude, delta = map(float,
                                                          choose_size_geocoder(
                                                              json_response_toponym))

search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

address_ll = f"{toponym_longitude},{toponym_lattitude}"

search_params = {
    "ll": address_ll,
    "text": "аптека",
    "type": "biz",
    # "results": str(10),     # Кол-во результатов в ответе
    "apikey": api_key,
    "lang": "ru_RU"
}

response = requests.get(search_api_server, params=search_params)
if not response:
    print(response.status_code)
    print(response.content)
    exit(-1)

json_response = response.json()

# Получаем организации
organizations = json_response["features"]
points = list()
for organization in organizations:
    # Название организации.
    org_name = organization["properties"]["CompanyMetaData"]["name"]
    # Адрес организации.
    org_address = organization["properties"]["CompanyMetaData"]["address"]
    # Часы работы
    org_hours = organization["properties"]["CompanyMetaData"]["Hours"]
    # Координаты
    org_longitude, org_lattitude, org_delta = choose_size_search_api(organization)

    try:
        twenty_four_hours_avaliable = org_hours["Availabilities"][0]["TwentyFourHours"]
        if twenty_four_hours_avaliable:
            point = f"{org_longitude},{org_lattitude},pm2gnm"
    except Exception:
        try:
            intervals = org_hours["Availabilities"][0]["Intervals"]
            point = f"{org_longitude},{org_lattitude},pm2blm"
        except Exception:
            point = f"{org_longitude},{org_lattitude},pm2grm"

    points.append(point)

delta = 0.05

# Собираем параметры для запроса к StaticMapsAPI:
map_params = {
    # позиционируем карту центром на наш исходный адрес
    "ll": f"{toponym_longitude},{toponym_lattitude}",
    "spn": ",".join([str(delta), str(delta)]),
    "l": "map",
    # добавим точки, чтобы указать найденную аптеку
    "pt": '~'.join(points)
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(response.content)).show()
