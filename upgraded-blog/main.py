from flask import Flask, render_template, request
import smtplib
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)

posts = requests.get('https://api.npoint.io/e42b353ee387383898c7').json()


@app.route('/')
def index():
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        # Send an email to me
        load_dotenv('../.env')
        my_email = os.getenv('email3')
        password = os.getenv('email_password_3')
        email = f"Subject: Fan Mail\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        with smtplib.SMTP("smtp.office365.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, to_addrs="almostnaturally@gmail.com", msg=email)

    return render_template('contact.html')


@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html', post=posts[post_id - 1])


if __name__ == '__main__':
    app.run(debug=True)
