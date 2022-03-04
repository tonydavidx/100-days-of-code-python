from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FILES_FOLDER'] = 'static/files/'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
# CREATE TABLE IN DB


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# Line below only required once, when creating DB.
# db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['Get', 'POST'])
def register():
    if request.method == "POST":
        new_name = request.form.get('name')
        new_email = request.form.get('email')
        new_password = request.form.get('password')

        if User.query.filter_by(email=new_email).first():
            flash("Email already exists")
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(
            new_password, method='pbkdf2:sha256', salt_length=8)
        new_user = User(name=new_name, email=new_email,
                        password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)

        return redirect(url_for('secrets'))

    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user_mail = request.form.get('email')
        user_password = request.form.get('password')

        user = User.query.filter_by(email=user_mail).first()

        if not user:
            flash('No user found with that email address.')
            return redirect(url_for('login'))

        elif not check_password_hash(user.password, user_password):
            flash('Incorrect password.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@login_required
@app.route('/download/<path:filename>', methods=['GET'])
def download(filename):
    return send_from_directory(app.config['FILES_FOLDER'], filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
