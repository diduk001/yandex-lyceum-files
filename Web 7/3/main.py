import os  # Для удаления ненужного изображения
import sys  # Для получения аргументов из командной строки (терминала)
from io import BytesIO  # Для перевода ответа API в изображение

import pygame  # Для отображения изображения в оконном приложении
import requests  # Для совершения запросов к API
from PIL import Image  # Для работы с изображением

# Пример использования:
'''
python3 main.py 37.677751 55.757718 0.016457 0.00619
'''

# Константные url для совершения запроса к API

STATIC_MAPS_API = "http://static-maps.yandex.ru/1.x/"
SEARCH_API = "https://search-maps.yandex.ru/v1/"
GEOCODER_API = "http://geocode-maps.yandex.ru/1.x/"

# Константы для минимального и максимального возможного масштаба карты

MIN_SPN = 0.0001
MAX_SPN = float(90)

# Констаны для хранения минимального и максимального значения широты и долготы

MIN_LONGITUDE = float(-180)
MAX_LONGITUDE = float(180)
MIN_LATTITUDE = float(-90)
MAX_LATTITUDE = float(90)

# Размер картинки (широта, высота)

STATIC_API_WIDTH = 600
STATIC_API_HEIGHT = 450


# Функция увеличения/уменьшения протяжённости. Принимает spn_ - протяжённость
# Функция увеличения протяжённости (уменьшения масштаба, на картинке помещается больше всего)

def increase_spn(spn_):
    spn = float(spn_)

    return str(min(spn * 2, MAX_SPN))


# Функция уменьшения протяжённости (увеличения масштаба, на картинке помещается меньше всего)


def reduce_spn(spn_):
    spn = float(spn_)

    return str(max(spn / 2, MIN_SPN))


# Функции изменения широты.
# longitude_ - широта (str)
# spn_ - протяжённость (str)


def change_longitude(longitude_, spn_):
    longitude = float(longitude_)
    spn = float(spn_)

    return str(longitude + spn / 2)


# Функция смещения камеры влево

def move_left(longitude, spn):
    return change_longitude(longitude, -spn)


# Функция смещения камеры вправо

def move_right(longitude, spn):
    return change_longitude(longitude, spn)

# Функции изменения долготы
# lattitude -

# Сохраняеи изображение temp.png по координатам и масштабу
# longitude, lattitude - широта и долгота
# spn1, spn2 - масштаб

def get_image(longitude, lattitude, spn1, spn2):
    print(spn1, spn2)

    # Собираем параметры для запроса

    static_api_params = {
        "ll": f"{longitude},{lattitude}",
        "spn": f"{spn1},{spn2}",
        "size": f"{STATIC_API_WIDTH},{STATIC_API_HEIGHT}",
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


# Достаём из командной строки широту, долготу, масштаб

longitude, lattitude, spn1, spn2 = sys.argv[1:]

# Инициализация pygame,таймера и fps

pygame.init()
clock = pygame.time.Clock()
fps = 60

# Ширина, Высота окна pygame в пикселях

screen_width = STATIC_API_WIDTH
screen_height = STATIC_API_HEIGHT

# Настройка размеров и заголовка окна pygame

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(f"{longitude}, {lattitude} на карте")

running = True
while running:

    # Обработка событий

    for event in pygame.event.get():

        # Выход

        if event.type == pygame.QUIT:
            running = False

        # Нажатие клавиши

        if event.type == pygame.KEYDOWN:

            # Обработка ещё одного сценария выхода

            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                running = False

            # Обработка изменения масштаба

            if event.key == pygame.K_PAGEUP:
                spn1, spn2 = increase_spn(spn1), increase_spn(spn2)

            if event.key == pygame.K_PAGEDOWN:
                spn1, spn2 = reduce_spn(spn1), reduce_spn(spn2)

            # Обработка перемещения камеры

    get_image(longitude, lattitude, spn1, spn2)

    # Загружаем изображение

    pygame_image = pygame.image.load("temp.png")

    #  Размещение изображения на экране

    screen.blit(pygame_image, (0, 0))

    pygame.display.flip()
    clock.tick(fps)

# Удаление временного файла изображения

os.remove("temp.png")

# Выход из программы

pygame.quit()
exit(0)
