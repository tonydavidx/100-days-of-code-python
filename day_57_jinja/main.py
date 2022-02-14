from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)
current_year = datetime.datetime.now().year

agify_endpoint = 'https://api.agify.io?'
genderize_endpoint = 'https://api.genderize.io?'

# print(agify_response.json())
# print(genderize_response.json())


@app.route('/')
def home_page():
    random_number = random.randint(1, 100)

    return render_template('index.html', number=random_number, year=current_year)


@app.route('/guess/<name>')
def guess_page(name):
    agify_response = requests.get(agify_endpoint, params={'name': name})
    genderize_response = requests.get(
        genderize_endpoint, params={'name': name})
    genrated_age = agify_response.json()['age']
    genrated_gender = genderize_response.json()['gender']
    return render_template('guess_page.html', name=name, age=genrated_age, gender=genrated_gender)


@app.route('/blog')
def blog_page():
    npoint = 'https://api.npoint.io/c790b4d5cab58020d391'
    posts_data = requests.get(npoint).json()
    return render_template('blog.html', posts=posts_data)


if __name__ == "__main__":
    app.run(debug=True)
