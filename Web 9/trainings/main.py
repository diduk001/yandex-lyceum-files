from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
