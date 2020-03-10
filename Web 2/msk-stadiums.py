import os
import sys

import pygame
import requests


def ll_by_address(address):
    ll_request_url = "https://geocode-maps.yandex.ru/1.x?apikey=40d1649f-0493-4b70-98ba" \
                     "-98533de7710b&geocode={}&format=json"

    response_ll = requests.get(ll_request_url.format(address))

    if not response_ll:
        return -1

    ll_json_resp = response_ll.json()

    return tuple(reversed(tuple(map(float, ll_json_resp["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"][
        "Point"]["pos"].split()))))


def address_to_json(address):
    return '+'.join(address.split())


pygame.init()
screen = pygame.display.set_mode((600, 450))

points = list()
for stadium in ["Волоколамское ш., 69, Москва, Россия", "Москва, Ленинградский просп., 36",
                "ул. Лужники, 24, стр. 1"]:
    longitude, latitude = ll_by_address(address_to_json(stadium))
    points.append(f"{latitude},{longitude}")

longitude_msk, latitude_msk = ll_by_address("Москва")

response = None
map_request = "http://static-maps.yandex.ru/1.x/?ll={},{}&spn={},{}&l=map&pt={}".format(
    latitude_msk, longitude_msk, 0.3, 0.3, '~'.join(points))

print(map_request)

response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
print(map_request)
print("Http статус:", response.status_code, "(", response.reason, ")")
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(map_file)
