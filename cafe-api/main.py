from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        """Convert a database table to a dictionary."""
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Records

@app.route("/random", methods=["GET"])
def get_random():
    """Return a random cafe from the database."""
    random_cafe = db.session.query(Cafe).order_by(db.func.random()).first()
    return jsonify(random_cafe.to_dict())


@app.route("/all", methods=["GET"])
def get_all():
    """Return all cafes from the database."""
    return jsonify(cafes=[cafe.to_dict() for cafe in db.session.query(Cafe).all()])


@app.route("/search", methods=["GET"])
def search():
    """Search for a cafe by location."""
    try:
        location = request.args.get("loc").capitalize()
    except AttributeError:
        return jsonify(error={"No Search Terms": "Please provide a valid search term."}), 400
    else:
        results = db.session.query(Cafe).filter_by(location=location).all()
        if results:
            return jsonify(cafes=[cafe.to_dict() for cafe in results])
        else:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})

# HTTP POST - Create Record


@app.route("/add", methods=["POST"])
def add_cafe():
    """Add a new cafe to the database."""
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    """Update the coffee price of a cafe."""
    try:
        price = request.args.get("new_price")
    except AttributeError:
        return jsonify(error={"No Data": "Please provide a valid price."}), 400
    else:
        cafe = db.session.query(Cafe).filter_by(id=cafe_id).first()
        if not cafe:
            return jsonify(error={"Not Found": "Sorry, a cafe with that id does not exist."}), 404
        else:
            cafe.coffee_price = price
            db.session.commit()
            return jsonify(response={"success": "Successfully updated the price of the cafe."})

# HTTP DELETE - Delete Record


@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    """Report a closed cafe and delete it from the database."""
    try:
        api_key = request.args.get("api_key")
    except AttributeError:
        return jsonify(error={"No Data": "Please provide a valid API key."}), 400
    else:
        if api_key != "secretkey":
            return jsonify(error={"Invalid API Key": "Please provide a valid API Key."}), 403
        else:
            cafe = db.session.query(Cafe).filter_by(id=cafe_id).first()
            if not cafe:
                return jsonify(error={"Not Found": "Sorry, a cafe with that id does not exist."}), 404
            else:
                db.session.delete(cafe)
                db.session.commit()
                return jsonify(response={"success": "Successfully reported and deleted the cafe."})


if __name__ == '__main__':
    app.run(debug=True)
