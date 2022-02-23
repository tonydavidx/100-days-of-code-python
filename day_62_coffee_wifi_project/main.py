import datetime
from email.policy import default
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = StringField('Location URL', validators=[
                               DataRequired(), URL(message='enter valid url', require_tld=True)])
    open_time = StringField('Open time', validators=[
        DataRequired()])

    closing_time = StringField('Closing time', validators=[DataRequired()])
    coffee_rating = StringField('Coffee rating', validators=[DataRequired()])
    wifi_rating = StringField('Wifi rating', validators=[DataRequired()])
    power_outlet = StringField(
        'Power outlet rating', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    new_data = []
    form = CafeForm()
    if form.validate_on_submit():
        print("👍 Validation successful ")
        new_data.append(form.cafe.data)
        new_data.append(form.location_url.data)
        new_data.append(form.open_time.data)
        new_data.append(form.closing_time.data)
        new_data.append(form.coffee_rating.data)
        new_data.append(form.wifi_rating.data)
        new_data.append(form.power_outlet.data)
        print(new_data)
        with open('cafe-data.csv', 'a', newline='', encoding='utf-8') as cafe_data:
            csv_writer = csv.writer(cafe_data)
            csv_writer.writerow(new_data)
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('./cafe-data.csv', newline='', encoding='utf_8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
