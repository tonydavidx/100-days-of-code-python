import random
from flask import Flask
app = Flask(__name__)

rand_number = random.randint(1, 9)


def add_image(image_url, width):
    return f'<img src="{image_url}"width={width}>'


@app.route('/<int:number>')
def guess(number):
    if number == rand_number:
        return f'<h1> That is Correct!</h1>\
            {add_image("https://media.giphy.com/media/UAXK9VGoJTbdcPgmcJ/giphy.gif",300)}'
    elif number < rand_number:
        return f'<h1> Too Low!</h1>\
            {add_image("https://media.giphy.com/media/cMJHOY2jGEHn2L48PC/giphy.gif", 400)}'
    elif number > rand_number:
        return f'<h1> Too High!</h1>\
            {add_image("https://media.giphy.com/media/3og0IuWMpDm2PdTL8s/giphy-downsized-large.gif", 400)}'


@ app.route("/")
def hello_world():
    return "<h1>Gues a number between 0 and 9</h1>\
        <img src='https://media.giphy.com/media/UDU4oUJIHDJgQ/giphy.gif' width=400>"


if __name__ == '__main__':
    app.run(debug=True)
