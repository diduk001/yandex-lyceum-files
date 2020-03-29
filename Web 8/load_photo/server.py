import os

from flask import Flask, url_for, request, redirect

app = Flask(__name__)


@app.route("/")
def mission_name():
    return f"""<!doctype html>
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
    return f"""<!doctype html>
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
    return f"""<!doctype html>
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
    return f"""<!doctype html>
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
                              <h4>Человечеству мала одна планета.</h4>
                            </div>
                            <div class="alert alert-success" role="alert">
                              <h4>Мы сделаем обитаемыми безжизненные пока планеты.</h4>
                            </div>
                            <div class="alert alert-danger" role="alert">
                              <h4>И начнем с Марса!</h4>
                            </div>
                            <div class="alert alert-warning" role="alert">
                              <h4>Присоединяйся!</h4>
                            </div>
                            
                          </body>
                        </html>"""


@app.route("/astronaut_selection", methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                                <html lang="en">
                                  <head>
                                    <meta charset="utf-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                    <link rel="stylesheet"
                                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                                    crossorigin="anonymous">
                                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                    <title>Пример формы</title>
                                  </head>
                                  <body>
                                    <h1>Анкета претендента</h1>
                                    <h2>на участие в миссии</h2>
                                    <div>
                                        <form class="login_form" method="post">
                                            <input type="text" class="form-control" id="name" placeholder="Введите своё имя" name="name">
                                            <input type="text" class="form-control" id="surname" placeholder="Введите свою фамилию" name="surname">
                                            <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email>
                                            <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">

                                            <div class="form-group">
                                                <label for="eduSelect">Какое у вас образование?</label>
                                                <select class="form-control" id="eduSelect" name="edu">
                                                  <option>Начальное</option>
                                                  <option>Основное общее</option>
                                                  <option>Среднее</option>
                                                  <option>Средне-специальное</option>
                                                  <option>Высшее</option>
                                                </select>
                                             </div>

                                            <label for="professions">Какая у вас профессия?</label>
                                            <div class="form-group form-check" id="professions">
                                                <div><input type="checkbox" class="form-check-input" id="researcher" name="researcherCheckbox">
                                                <label class="form-check-label" for="researcher">Исследователь</label></div>

                                                <div><input type="checkbox" class="form-check-input" id="builder" name="builderCheckbox">
                                                <label class="form-check-label" for="builder">Строитель</label></div>

                                                <div><input type="checkbox" class="form-check-input" id="pilot" name="pilotCheckbox">
                                                <label class="form-check-label" for="pilot">Пилот</label></div>

                                                <div><input type="checkbox" class="form-check-input" id="meteorologist" name="meteorologistCheckbox">
                                                <label class="form-check-label" for="meteorologist">Меторолог</label></div>

                                                <div><input type="checkbox" class="form-check-input" id="engineer" name="engineerCheckbox">
                                                <label class="form-check-label" for="engineer">Инженер</label></div>

                                                <div><input type="checkbox" class="form-check-input" id="doctor" name="doctorCheckbox">
                                                <label class="form-check-label" for="doctor">Доктор</label></div>

                                                <div><input type="checkbox" class="form-check-input" id="biologist" name="biologistCheckbox">
                                                <label class="form-check-label" for="biologist">Биолог</label></div>

                                                <div><input type="checkbox" class="form-check-input" id="guardian" name="guardianCheckbox">
                                                <label class="form-check-label" for="guardian">Охранник</label></div>
                                            </div>                                        

                                            <div class="form-group">
                                                <label for="form-check">Укажите пол</label>
                                                <div class="form-check">
                                                  <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                                  <label class="form-check-label" for="male">
                                                    Мужской
                                                  </label>
                                                </div>

                                                <div class="form-check">
                                                  <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                                  <label class="form-check-label" for="female">
                                                    Женский
                                                  </label>
                                                </div>
                                            </div>

                                            <div class="form-group">
                                                <label for="about">Почему вы хотите принять участие в миссии?</label>
                                                <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                            </div>

                                            <div class="form-group form-check">
                                                <input type="checkbox" class="form-check-input" id="stayOnMars" name="stay_on_mars">
                                                <label class="form-check-label" for="stayOnMars">Готовы остаться на Марсе?</label>
                                            </div>
                                            <button type="submit" class="btn btn-primary">Записаться</button>
                                        </form>
                                    </div>
                                  </body>
                                </html>'''
    elif request.method == "POST":
        return mission_name()


@app.route("/choice/<planet_name>")
def choice(planet_name):
    return f"""<!doctype html>
                            <html lang="ru">
                              <head>
                                <meta charset="utf-8">                            
                                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />                    
                                <title>Колонизация</title>
                              </head>
                              <body>
                                <h1>Моё предложение: {planet_name}</h1>
                                <h2>Это крутая планета</h2>
                                <div class="alert alert-primary" role="alert">
                                  <h4>На ней много необходимых ресурсов</h4>
                                </div>
                                <div class="alert alert-secondary" role="alert">
                                  <h4>На ней есть вода и атмосфера</h4>
                                </div>
                                <div class="alert alert-success" role="alert">
                                  <h4>Не ней есть магнитное поле, хоть и небольшое</h4>
                                </div>
                                <div class="alert alert-danger" role="alert">
                                  <h4>Наконец, она просто красивая!</h4>
                                </div>
                                <div class="alert alert-warning" role="alert">
                                  <h4>Присоединяйся!</h4>
                                </div>

                              </body>
                            </html>"""


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return f"""<!doctype html>
                                <html lang="ru">
                                  <head>
                                    <meta charset="utf-8">                            
                                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />                    
                                    <title>Колонизация</title>
                                  </head>
                                  <body>
                                    <h1>Результаты отбора</h1>
                                    <h2>Претендента на участие в миссии {nickname}</h2>
                                    <div class="alert alert-success" role="alert">
                                      <h4>Поздравляем!</h4>
                                    </div>
                                    <div class="alert alert-success" role="alert">
                                      <h4>После {level} этапа отбора ваш рейтинг составил {rating}</h4>
                                    </div>
                                    <div class="alert alert-danger" role="alert">
                                      <h4>Желаем удачи в {level + 1} этапе отбора</h4>
                                    </div>

                                  </body>
                                </html>"""


def allowed_image(filename):
    ALLOWED_IMAGE_EXTENSIONS = ["PNG", "JPG", "JPEG", "GIF"]

    if filename == "":
        return False

    if '.' not in filename:
        return False

    extension = filename.split('.')[1]

    if extension.upper() not in ALLOWED_IMAGE_EXTENSIONS:
        return False

    return True


@app.route("/load_photo", methods=["GET", "POST"])
def load_photo():
    if request.method == 'GET':
        if len(os.listdir(os.path.join("static/img/uploads"))) == 0:
            return f'''<!doctype html>
                                        <html lang="en">
                                          <head>
                                            <meta charset="utf-8">
                                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                             <link rel="stylesheet"
                                             href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                                             integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                                             crossorigin="anonymous">
                                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                            <title>Пример загрузки файла</title>
                                          </head>
                                          <body>
                                            <h1>Загрузим файл</h1>
                                            <form method="post" enctype="multipart/form-data">
                                                <h3><label for="photo">Выберите файл</label></h3>
                                                <h3><input accept="image/*" type="file" class="form-control-file" id="photo" name="image"></h3>
                                                <br></br>
                                                <h3><button type="submit" class="btn btn-primary">Отправить</button></h3>
                                            </form>
                                          </body>
                                        </html>'''
        else:
            img_name = os.listdir(os.path.join("static/img/uploads"))[0]
            print(url_for("static", filename="img/uploads/" + img_name))
            return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                 <link rel="stylesheet"
                                 href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                                 integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                                 crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Пример загрузки файла</title>
                              </head>
                              <body>
                                <h1>Загрузим файл</h1>
                                <form method="post" enctype="multipart/form-data">
                                    <h3><label for="photo">Выберите файл</label></h3>
                                    <h3><input accept="image/*" type="file" class="form-control-file" id="photo" name="image"></h3>
                                    <br></br>
                                    <h3><button type="submit" class="btn btn-primary">Отправить</button></h3>
                                </form>
                                <br></br>
                                <img src={url_for("static", filename="img/uploads/" + img_name)}>
                              </body>
                            </html>'''

    elif request.method == 'POST':
        if request.files:
            image = request.files["image"]

            if not allowed_image(image.filename):
                return redirect(request.url)

            filename, ext = image.filename.split('.')

            os.chdir("static")
            os.chdir("img")
            os.chdir("uploads")
            if len(os.listdir(os.getcwd())) != 0:
                for item in os.listdir(os.getcwd()):

                    try:
                        os.remove(os.path.join(os.path.abspath(os.getcwd())) + '/' + item)

                    except FileNotFoundError:
                        continue

            filename, ext = image.filename.split('.')
            image.filename = "uploaded." + ext
            image.save(os.path.join(os.path.abspath(os.getcwd())) + '/' + image.filename)

            os.chdir("..")
            os.chdir("..")
            os.chdir("..")

    return redirect(request.url)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
