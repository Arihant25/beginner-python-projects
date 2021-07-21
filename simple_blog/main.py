from flask import Flask, render_template
import requests


app = Flask(__name__)
posts = requests.get("https://api.npoint.io/4af156202f984d3464c3").json()


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route('/post/<int:id>')
def get_post(id):
    return render_template("post.html", id=id, post=posts[id - 1])


if __name__ == "__main__":
    app.run(debug=True)
