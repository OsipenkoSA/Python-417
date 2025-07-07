from flask import Flask, render_template

app = Flask(__name__)

menu = [
    {"name": "Главная", "url": "index"},
    {"name": "О нас", "url": "about"},
    {"name": "Обратная связь", "url": "contact"},
]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Главная", menu=menu)


@app.route("/about")
def about():
    return render_template("about.html", title="О нас", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
