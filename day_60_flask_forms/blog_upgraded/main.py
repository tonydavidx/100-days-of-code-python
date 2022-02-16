from flask import Flask, render_template, request
import requests
import smtplib
import os
app = Flask(__name__)

data = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()


@app.route('/')
def home():
    return render_template('index.html', posts=data)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        data = request.form
        username = data['name']
        mail = data['email']
        phone = data['phone']
        msg = data['message']
        print(username, mail, phone, msg)
        send_mail(username, mail, phone, msg)
        return render_template('contact.html', msg_sent=True)

    return render_template('contact.html', msg_sent=False)


def send_mail(name, email, phone, msg):
    message = f'subject: New Message\n\nFrom: {name} ({email})\nPhone: {phone}\n\n{msg}'
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(os.getenv('MAIL_USERNAME'), os.getenv('MAIL_PASSWORD'))
        smtp.sendmail(msg=message, from_addr=email,
                      to_addrs=os.getenv('MAIL_USERNAME'))


@app.route('/post/<int:id>')
def show_post(id):
    for post in data:
        if post['id'] == id:
            return render_template('post.html', post=post)


if __name__ == '__main__':
    app.run(debug=True)
