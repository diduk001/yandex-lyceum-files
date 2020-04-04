from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "0d645377e31ab6b5847ec817bac4aaf8"


class LoginForm(FlaskForm):
    astronaut_id = StringField('id астронавта', validators=[DataRequired()])
    astronaut_pass = PasswordField('пароль астронавта', validators=[DataRequired()])
    captain_id = StringField('id капитана', validators=[DataRequired()])
    captain_pass = PasswordField('пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Допуск')


@app.route("/")
@app.route("/index")
def index():
    title = "Миссия колонизации марса"
    return render_template("base.html", title=title)


@app.route("/training/<prof>")
def training(prof):
    params = {}
    params["title"] = "Тренировки в полёте"

    if "строитель" in prof.lower() or "инженер" in prof.lower():
        params["training"] = "Инженерные тренировки"
    else:
        params["training"] = "Научные симуляторы"

    return render_template("trainings.html", **params)


@app.route("/list_prof/<list>")
def list_prof(list):
    return render_template("list_prof.html", title="Список профессий", list=list)


@app.route("/answer")
@app.route("/auto_answer")
def answer():
    params = dict()
    params["title"] = "Ваши данные"
    return render_template("auto_answer.html", **params)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        return redirect("/")
    return render_template("login.html", title="Аварийный доступ", form=form)


@app.route("/distribution")
def distribution():
    params = dict()
    params["title"] = "Размещение"
    return render_template("distribution.html", **params)


@app.route("/table/<sex>/<int:age>")
def table(sex, age):
    params = dict()
    params["title"] = "Каюта"
    if age < 21:
        params["alien_file_path"] = url_for("static", filename="img/baby.jpeg")
        if sex == "male":
            params["color_file_path"] = url_for("static", filename="img/boy.png")
        elif sex == "female":
            params["color_file_path"] = url_for("static", filename="img/girl.png")
    else:
        params["alien_file_path"] = url_for("static", filename="img/adult.jpg")
        if sex == "male":
            params["color_file_path"] = url_for("static", filename="img/man.png")
        elif sex == "female":
            params["color_file_path"] = url_for("static", filename="img/woman.png")
    return render_template("table.html", **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
