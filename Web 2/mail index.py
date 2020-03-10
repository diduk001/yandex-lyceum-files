import requests

url = "https://geocode-maps.yandex.ru/1.x?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode" \
      "={}&format=json"

response = requests.get(url.format("Москва,+ул.Петровка,+38"))
json_resp = response.json()
components = address = \
    json_resp["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"][
        "metaDataProperty"]["GeocoderMetaData"]["Address"]
print(components["postal_code"])