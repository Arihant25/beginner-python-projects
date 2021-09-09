from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure login manager
login_manager = LoginManager()
login_manager.init_app(app)

# CREATE TABLE IN DB


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    is_authenticated = True

# Create user loader function required by flask-login


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        # Get the name and email from the form
        name = request.form['name']
        email = request.form['email']

        # Check if user already exists
        if db.session.query(User).filter_by(email=email).first():
            flash('There\'s already an account with that email. Try logging in instead.')
            return redirect(url_for('login'))

        # Hash the password before storing it in the database
        hashed_password = generate_password_hash(
            request.form['password'], method='pbkdf2:sha256', salt_length=8)

        # Create a new user and add them to the database
        new_user = User(
            name=name,
            email=email,
            password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        # Log the new user in and redirect to the secret page
        login_user(new_user)
        return redirect(url_for('secrets', name=new_user.name))

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        # Get the email and password from the form
        email = request.form['email']
        password = request.form['password']

        # Check if the user exists in the database
        user = db.session.query(User).filter_by(email=email).first()

        if user:
            # Check if the password is correct
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('secrets', name=user.name))
            else:
                flash('Incorrect password. Try again?')
                return redirect(url_for('login'))
        else:
            flash('No user found with that email address. Have you registered yet?')
            return redirect(url_for('login'))

    return render_template("login.html")


@app.route('/secrets/<name>')
@login_required
def secrets(name):
    return render_template("secrets.html", name=name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(directory="static/files", path="cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
