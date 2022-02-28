from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
tmdb_api = os.getenv('TMDB_KEY')
tmdb_search = 'https://api.themoviedb.org/3/search/movie'


class AddMovieForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    submit = SubmitField("Search")


class Rating_Form(FlaskForm):
    rating = FloatField('Your Rating', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Submit')


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(1000), nullable=False)
    img_url = db.Column(db.String(100), nullable=False)


db.create_all()


@app.route("/")
def home():
    all_movies = Movie.query.all()
    return render_template("index.html", movies=all_movies)


@app.route('/add', methods=['GET', 'POST'])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        title = form.title.data
        search_movie = requests.get(
            tmdb_search, params={'api_key': tmdb_api, 'query': title})
        print(search_movie.status_code)
        # results = search_movie.json()['results']
        # print(results)
        # return render_template('select.html', results=results)
    return render_template('add.html', form=form)


# def add_movie_data():
#     id = request.args.get('id')
#     movie_data = requests.get(
#         f'https://api.themoviedb.org/3/movie/{id}?api_key={tmdb_api}&language=en-US').json()
#     print(movie_data)


@app.route('/update', methods=['GET', 'POST'])
def update():
    update_form = Rating_Form()
    movie_id = request.args.get('id')
    selected_movie = Movie.query.get(movie_id)
    if request.method == "POST":
        selected_movie.rating = update_form.rating.data
        selected_movie.review = update_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=selected_movie, form=update_form)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    selected_movie = Movie.query.get(movie_id)
    db.session.delete(selected_movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
