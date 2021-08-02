from flask import Flask, render_template
import requests

app = Flask(__name__)

posts = requests.get('https://api.npoint.io/e42b353ee387383898c7').json()


@app.route('/')
def index():
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html', post=posts[post_id - 1])


if __name__ == '__main__':
    app.run(debug=True)
