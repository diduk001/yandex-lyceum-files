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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
