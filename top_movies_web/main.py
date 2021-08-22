# Flask
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
# WTForms
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField
# Requests
import requests
from dotenv import load_dotenv
from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBAO6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
Bootstrap(app)
db = SQLAlchemy(app)
# Get the API key from the .env file
load_dotenv('../.env')
api_key = getenv('tmdb_api_key')


class Movie(db.Model):
    """Contains data on Movies"""
    # Create the various fields and set their properties and types
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(250), nullable=True)
    rating = db.Column(db.Float(), nullable=True)
    review = db.Column(db.String(500), nullable=True)
    img_url = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return f"Movie({self.title})"


class EditForm(FlaskForm):
    """Form for editing movie information"""
    rating = StringField(label='Your Rating (out of 10)',
                         validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Done')


class AddForm(FlaskForm):
    """Form for adding a movie"""
    title = StringField(label='Title of the Movie',
                        validators=[DataRequired()])
    submit = SubmitField(label='Add')


# Create the database
db.create_all()


@ app.route("/")
def home():
    """Get all movies from the database and display them"""
    all_movies = db.session.query(Movie).order_by(Movie.rating).all()
    return render_template("index.html", all_movies=all_movies)


@ app.route("/edit/<int:movie_id>", methods=['GET', 'POST'])
def edit(movie_id):
    """Edit a movie"""
    movie = db.session.query(Movie).get(movie_id)
    form = EditForm()
    if form.validate_on_submit():
        # Get the data from the form
        new_rating = request.form['rating']
        new_review = request.form['review']
        # Check if any fields have been changed and accordingly update the database
        movie.rating = new_rating
        movie.review = new_review
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route('/delete/<int:movie_id>')
def delete(movie_id):
    """Delete a movie from the database"""
    movie = db.session.query(Movie).get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    """Add a movie to the database"""
    form = AddForm()
    if form.validate_on_submit():
        # Get the data from the form
        title = request.form['title']
        # Search for movies using the TMDB API
        url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=en-US&page=1&query={title}"
        response = requests.get(url).json()
        return render_template("select.html", response=response)
    return render_template("add.html", form=form)


@app.route('/search_movie/<int:movie_id>')
def search_movie(movie_id):
    """Search for a movie using the TMDB API"""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response = requests.get(url).json()
    # Add the new movie
    new_movie = Movie(title=response['title'],
                      year=response['release_date'][:4],
                      description=response['overview'],
                      img_url="https://image.tmdb.org/t/p/w500//" + str(response['poster_path']))
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', movie_id=new_movie.id))


if __name__ == '__main__':
    app.run()
