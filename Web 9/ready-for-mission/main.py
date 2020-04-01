from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    title = "Миссия колонизации марса"
    return render_template("base.html", title=title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
