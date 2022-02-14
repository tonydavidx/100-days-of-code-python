from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

npoint = 'https://api.npoint.io/c790b4d5cab58020d391'
post_data = requests.get(npoint).json()

post_objects = []
for data in post_data:
    post_obj = Post(data['id'], data['title'], data['subtitle'], data['body'])
    post_objects.append(post_obj)


@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)


@app.route('/post/<int:id>')
def show_post(id):
    requested_post = None
    for post in post_objects:
        if post.id == id:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
