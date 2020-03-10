import requests

url = "https://geocode-maps.yandex.ru/1.x?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode" \
      "=Москва,+Красная+пл-дь,+1&format=json"
response = requests.get(url)
json_resp = response.json()

address = json_resp["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"][
    "metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]

ans = [name['name'] for name in address]
print(', '.join(ans))
