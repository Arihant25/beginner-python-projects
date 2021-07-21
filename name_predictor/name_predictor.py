from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:name>')
def get_name(name):
    age = requests.get("https://api.agify.io?name=" + name).json()["age"]
    gender = requests.get(
        "https://api.genderize.io/?name=" + name).json()["gender"]
    return render_template('name.html', name=name.title(), age=age, gender=gender)


if __name__ == '__main__':
    app.run(debug=True)
