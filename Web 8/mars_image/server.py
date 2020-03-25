from flask import Flask

app = Flask(__name__)


@app.route("/")
def mission_name():
    return f"""<!doctype html>
                    <html lang="ru">
                      <head>
                        <meta charset="utf-8">
                        <title>Колонизация Марса</title>
                      </head>
                      <body>
                        <h1>Миссия Колонизация Марса</h1>
                      </body>
                    </html>"""


@app.route("/index")
def mission_slogan():
    return f"""<!doctype html>
                    <html lang="ru">
                      <head>
                        <meta charset="utf-8">
                        <title>Колонизаця Марса</title>
                      </head>
                      <body>
                        <h1>И на Марсе будут яблони цвести!</h1>
                      </body>
                    </html>"""


@app.route("/promotion")
def promotion():
    return f"""<!doctype html>
                    <html lang="ru">
                      <head>
                        <meta charset="utf-8">
                        <title>Колонизаця Марса</title>
                      </head>
                      <body>
                        <h1>Рекламная комания</h1>
                        <br></br>
                        <p>Человечество вырастает из детства.</p>
                        <p>Человечеству мала одна планета.</p>
                        <p>Мы сделаем обитаемыми безжизненные пока планеты.</p>
                        <p>И начнем с Марса!</p>
                        <p>Присоединяйся!</p>
                      </body>
                    </html>"""


@app.route("/image_mars")
def image_mars():
    return f"""<!doctype html>
                        <html lang="ru">
                          <head>
                            <meta charset="utf-8">
                            <title>Привет, Марс!</title>
                          </head>
                          <body>
                            <h1>Жди нас, Марс!</h1>
                            <p><img src=https://astroson.com/wp-content/uploads/2017/03/Mars.png  
                            alt="Изображение Марса"></p>
                            <p>Вот она, какая, Красная Планета</p>
                          </body>
                        </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
