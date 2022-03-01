from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import true
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
import requests
import os

agent = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'}

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
    ranking = IntegerField('Rank', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Submit')


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(1000), nullable=True)
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
        while True:
            try:
                search_movie = requests.get(
                    tmdb_search, params={'api_key': tmdb_api, 'query': title})
                break
            except Exception as e:
                print(f'Error: {e}')
        results = search_movie.json()['results']
        return render_template('select.html', results=results)
    return render_template('add.html', form=form)


@app.route('/find', methods=['GET', 'POST'])
def find_movie():
    id = request.args.get('id')
    while True:
        try:
            movie_data = requests.get(
                f'https://api.themoviedb.org/3/movie/{id}?api_key={tmdb_api}&language=en-US').json()
            break
        except Exception as e:
            print(f'Error: {e}')
    new_movie = Movie(
        title=movie_data['original_title'],
        year=movie_data['release_date'][:4],
        rating=movie_data['vote_average'],
        description=movie_data['overview'],
        img_url=f'https://image.tmdb.org/t/p/w500{movie_data["poster_path"]}',
        review='',
        ranking=10
    )
    db.session.add(new_movie)
    db.session.commit()
    movie = Movie.query.filter_by(title=movie_data['original_title']).first()
    movie_id = movie.id
    return redirect(url_for('update', id=movie_id))


@app.route('/update', methods=['GET', 'POST'])
def update():
    update_form = Rating_Form()
    movie_id = request.args.get('id')
    selected_movie = Movie.query.get(movie_id)
    if request.method == "POST":
        selected_movie.ranking = update_form.ranking.data
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
    app.run(debug=True, use_reloader=True)
