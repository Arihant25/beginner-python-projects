from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


app = Flask(__name__)

# Location of the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Flask Secret Key
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBYox7C0sKR6b'

db = SQLAlchemy(app)
Bootstrap(app)


class Book(db.Model):
    """Database model for representing a book."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"{self.title} - {self.author} - {self.rating}/10"


class EditForm(FlaskForm):
    """Create a form object with WTForms."""
    rating = StringField('Edit Rating', validators=[DataRequired()])
    submit = SubmitField('Submit')


# Create the database
db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # Add a book to the database
        new_book = Book(title=request.form["title"],
                        author=request.form["author"],
                        rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()

        # Redirect to homepage
        return redirect(url_for("home"))
    return render_template('add.html')


@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    form = EditForm()
    # When the form is submitted
    if form.validate_on_submit():
        # Get the updated rating
        new_rating = form.rating.data
        # Get the book with the given id
        book = Book.query.get(book_id)
        # Update the book's rating
        book.rating = new_rating
        # Save the book to the database
        db.session.commit()
        # Redirect to the homepage
        return redirect(url_for("home"))
    return render_template('edit.html', book_id=Book.query.get(book_id), form=form)


@app.route('/delete/<int:book_id>')
def delete(book_id):
    # Get the book with the given id
    book = Book.query.get(book_id)
    # Delete the book from the database
    db.session.delete(book)
    db.session.commit()
    # Redirect to the homepage
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
