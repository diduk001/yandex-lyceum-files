import os  # Для удаления ненужного изображения
import sys  # Для получения аргументов из командной строки (терминала)
from io import BytesIO  # Для перевода ответа API в изображение

import pygame  # Для отображения изображения в оконном приложении
import requests  # Для совершения запросов к API
from PIL import Image  # Для работы с изображением

# Пример использования:
# python3 main.py 37.677751 55.757718 0.016457 0.00619

# Константные url для совершения запроса к API

STATIC_MAPS_API = "http://static-maps.yandex.ru/1.x/"
SEARCH_API = "https://search-maps.yandex.ru/v1/"
GEOCODER_API = "http://geocode-maps.yandex.ru/1.x/"

# Достаём из командной строки широту, долготу, масштаб

longitude, lattitude, spn1, spn2 = sys.argv[1:]

# Размер картинки (широта, высота)

static_api_width = 600
static_api_height = 450

# Собираем параметры для запроса

static_api_params = {
    "ll": f"{longitude},{lattitude}",
    "spn": f"{spn1},{spn2}",
    "size": f"{static_api_width},{static_api_height}",
    "l": "map"
}

# Совершаем запрос к Static API

static_api_response = requests.get(STATIC_MAPS_API, static_api_params)

# Обрабатываем ошибку запроса

if not static_api_response:
    print("static api error")
    print(static_api_response.status_code)
    print(static_api_response.content)
    exit(-1)

# Получаем изображение из запроса, сохраняем его и переводим в pygame.Surface

pil_image = Image.open(BytesIO(static_api_response.content))
pil_image.save("temp.png")

pygame_image = pygame.image.load("temp.png")

# Инициализация pygame

pygame.init()

# Ширина, Высота окна pygame в пикселях

screen_width = static_api_width
screen_height = static_api_height

# Настройка размеров и заголовка окна pygame

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(f"{longitude}, {lattitude} на карте")

running = True
while running:

    # Обработка события на выход

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #  Размещение изображения на экране

    screen.blit(pygame_image, (0, 0))

    pygame.display.flip()

# Удаление временного файла изображения

os.remove("temp.png")

# Выход из программы

pygame.quit()
exit(0)
