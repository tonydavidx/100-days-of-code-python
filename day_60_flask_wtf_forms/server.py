from attr import validate
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[
                             DataRequired(), Length(min=8, max=16)])
    submit = SubmitField()


app = Flask(__name__)
app.secret_key = 'thisisasecretkey'
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@gmail.com':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form,)


if __name__ == '__main__':
    app.run(debug=True)
