import requests

url = "https://geocode-maps.yandex.ru/1.x?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode" \
      "={}&format=json"

cities = ["Барнаул", "Мелеуз", "Йошкар-Ола"]

for city in cities:
    response = requests.get(url.format(city))
    json_resp = response.json()
    components = address = \
        json_resp["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"][
            "metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]
    region = components[2]["name"]
    city = components[4]["name"]
    print(f'{city} - {region}')
