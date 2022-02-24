from enum import unique
import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, unique=True, nullable=False)


# db.drop_all()
# db.create_all()

lotr = Book(title='Lord of the rings',
            author='Tolkien', rating=10.0)

harry_potter = Book(title='Harry Potter',
                    author='Rowling', rating=7.0)
mythos = Book(title='Mythos',
                    author='Stphen fry', rating=9.0)

# db.session.add(harry_potter)
# db.session.add(lotr)
# db.session.add(mythos)
# db.session.commit()

# CRUD
# Read
all_books = db.session.query(Book).all()
book = db.session.query(Book).filter_by(title='Lord of the rings').first()
print(all_books)
print(book.title)
# Update
book_to_update = Book.query.filter_by(title='Lord of the rings').first()
book_to_update.title = 'The Lord of the Rings'
db.session.commit()
# delete
book_id = 1
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()


@app.route('/')
def home():
    return 'Hello World'


if __name__ == "__main__":
    app.run(debug=True)
