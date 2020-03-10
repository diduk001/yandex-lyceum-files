import os

import pygame
import requests

points = [30.30025005, 59.9367844,
          30.30016422, 59.93712838,
          30.31123638, 59.94164275,
          30.31394005, 59.94196518,
          30.31445503, 59.9449314,
          30.3126955, 59.94589859,
          30.29316902, 59.94684425,
          30.26887894, 59.9546235,
          30.26621819, 59.95608459,
          30.26274204, 59.95709442,
          30.25360107, 59.95831907,
          30.20890474, 59.96721255,
          29.91388321, 59.89152036]

response = None
map_request = "http://static-maps.yandex.ru/1.x/?pl={}&l=map".format(
    ','.join(list(map(str, points))))
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
print(map_request)
print("Http статус:", response.status_code, "(", response.reason, ")")

# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)
