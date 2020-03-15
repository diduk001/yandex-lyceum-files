import sys
from io import BytesIO

import requests
from PIL import Image

# Пример использования:
# python3 main.py 37.677751 55.757718 0.016457 0.00619

# Константные url для совершения запроса к API

STATIC_MAPS_API = "http://static-maps.yandex.ru/1.x/"
SEARCH_API = "https://search-maps.yandex.ru/v1/"
GEOCODER_API = "http://geocode-maps.yandex.ru/1.x/"

# Достаём из командной строки широту, долготу, масштаб

longitude, lattitude, spn1, spn2 = sys.argv[1:]

# Размер картинки (широта, высота)

size_width = 600
size_height = 450

# Собираем параметры для запроса

static_api_params = {
    "ll": f"{longitude},{lattitude}",
    "spn": f"{spn1},{spn2}",
    "size": f"{size_width},{size_height}",
    "l": "map"
}

# Совершаем запрос к Static API

static_api_response = requests.get(STATIC_MAPS_API, static_api_params)

# Обрабатываем ошибку

if not static_api_response:
    print("static api error")
    print(static_api_response.status_code)
    print(static_api_response.content)
    exit(-1)

Image.open(BytesIO(static_api_response.content)).show()
