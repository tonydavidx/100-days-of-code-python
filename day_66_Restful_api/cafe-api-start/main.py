from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

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
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/random', methods=['GET'])
def random_route():
    random_cafe = random.choice(Cafe.query.all())
    random_cafe = random_cafe.to_dict()
    print(random_cafe)
    return jsonify(cafe=random_cafe)


@app.route('/all', methods=['GET'])
def all():
    all_cafes = Cafe.query.all()
    cafes = []
    for cafe in all_cafes:
        cafe.to_dict()
        cafes.append(cafe.to_dict())
    return jsonify(cafes=cafes)


@app.route('/search', methods=['GET'])
def search():
    search_term = request.args.get('loc')
    all_cafes = Cafe.query.all()
    cafes = []
    error = {
        'error': 'No cafes found'
    }
    for cafe in all_cafes:
        if search_term in cafe.location:
            cafes.append(cafe.to_dict())

    if cafes is not []:
        return jsonify(cafes=cafes)
    else:
        return jsonify(error)


# HTTP GET - Read Record

# HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add():
    new_cafe = Cafe(
        name=request.form.get('name'), map_url=request.form.get('map_url'), img_url=request.form.get('img_url'),
        location=request.form.get('loc'), seats=request.form.get('seats'), has_toilet=bool(request.form.get('toilet')),
        has_wifi=bool(request.form.get('wifi')), has_sockets=bool(request.form.get('sockets')), can_take_calls=bool(request.form.get('calls')), coffee_price=request.form.get('coffee_price')
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={'success': 'Cafe added successfully'})

# HTTP PUT/PATCH - Update Record


@app.route('/update/<int:id>', methods=['PATCH'])
def update(id):
    cafe = Cafe.query.get(id)
    if cafe:
        cafe.coffee_price = request.form.get('new_price')
        db.session.commit()
        return jsonify(response={'success': 'Cafe updated successfully'}), 200
    else:
        return jsonify(response={'error': 'Cafe not found'}), 404
# HTTP DELETE - Delete Record


@app.route('/report-closed/<int:id>', methods=['DELETE'])
def report_closed(id):
    api_key = request.args.get('api_key')
    if api_key == 'SecretKey':
        cafe = Cafe.query.get(id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={'success': 'Cafe deleted successfully'}), 200
        else:
            return jsonify(response={'error': 'Cafe not found'}), 404
    else:
        return jsonify(response={'error': 'Invalid API key'}), 401


if __name__ == '__main__':
    app.run(debug=True)
