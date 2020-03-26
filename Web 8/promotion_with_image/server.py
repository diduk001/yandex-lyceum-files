from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def mission_name():
    return """<!doctype html>
                    <html lang="ru">
                      <head>
                        <meta charset="utf-8">                            
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Колонизация Марса</title>
                      </head>
                      <body>
                        <h1>Миссия Колонизация Марса</h1>
                      </body>
                    </html>"""


@app.route("/index")
def mission_slogan():
    return """<!doctype html>
                    <html lang="ru">
                      <head>
                        <meta charset="utf-8">                            
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Колонизаця Марса</title>
                      </head>
                      <body>
                        <h1>И на Марсе будут яблони цвести!</h1>
                      </body>
                    </html>"""


@app.route("/promotion")
def promotion():
    return """<!doctype html>
                    <html lang="ru">
                      <head>
                        <meta charset="utf-8">                            
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
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
    return """"<!doctype html>
                        <html lang="ru">
                          <head>
                            <meta charset="utf-8">                            
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Привет, Марс!</title>
                          </head>
                          <body>
                            <h1>Жди нас, Марс!</h1>
                            <p><img src=https://astroson.com/wp-content/uploads/2017/03/Mars.png  
                            alt="Изображение Марса"></p>
                            <p>Вот она, какая, Красная Планета</p>
                          </body>
                        </html>"""


@app.route("/promotion_image")
def promotion_image():
    return f"""<!doctype html>
                        <html lang="ru">
                          <head>
                            <meta charset="utf-8">                            
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />                    
                            <title>Колонизация</title>
                          </head>
                          <body>
                            <h1>Жди нас, Марс!</h1>
                            <p><img src={url_for("static", filename="img/Mars.png")}  
                            alt="Изображение Марса"></p>
                            <div class="alert alert-primary" role="alert">
                              <h4>Человечество вырастает из детства</h4>
                            </div>
                            <div class="alert alert-secondary" role="alert">
                              <h4>Человечество вырастает из детства</h4>
                            </div>
                            <div class="alert alert-success" role="alert">
                              <h4>Человечество вырастает из детства</h4>
                            </div>
                            <div class="alert alert-danger" role="alert">
                              <h4>Человечество вырастает из детства</h4>
                            </div>
                            <div class="alert alert-warning" role="alert">
                              <h4>Человечество вырастает из детства</h4>
                            </div>
                            
                          </body>
                        </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
