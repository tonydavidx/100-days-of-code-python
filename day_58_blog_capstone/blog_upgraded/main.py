from flask import Flask, render_template
import requests
app = Flask(__name__)

data = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()


@app.route('/')
def home():
    return render_template('index.html', posts=data)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:id>')
def show_post(id):
    for post in data:
        if post['id'] == id:
            return render_template('post.html', post=post)


if __name__ == '__main__':
    app.run(debug=True)
