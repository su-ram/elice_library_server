from elice_library import db
from datetime import datetime
from flask_login import UserMixin

class User(UserMixin,db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(30), primary_key=True)
    password = db.Column(db.String(100))
    image = db.Column(db.String(100))


class Book(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_name = db.Column(db.String(100))
    publisher = db.Column(db.String(30))
    author = db.Column(db.String(30))
    publication_date = db.Column(db.DATE)
    pages = db.Column(db.Integer)
    description = db.Column(db.TEXT)
    link = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    isbn = db.Column(db.BIGINT)
    quantity = db.Column(db.Integer)
    image_path = db.Column(db.String(100))


class Rental(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey("user.id"))
    bookid = db.Column(db.Integer, db.ForeignKey("book.id"))
    book = db.relationship('Book')
    rental_date = db.Column(db.Date, nullable=False, default=datetime.today().date())
    return_date = db.Column(db.Date, nullable=True, default=None)


class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bookid = db.Column(db.Integer, db.ForeignKey("book.id"))
    userid = db.Column(db.Integer, db.ForeignKey("user.id"))
    __table_args__ = ((db.UniqueConstraint('bookid','userid',name='uniqe_bookid_userid'),))
    user = db.relationship('User')
    content = db.Column(db.TEXT)
    create_date = db.Column(db.DateTime, default=datetime.today())


class Rating(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    commentid = db.Column(db.Integer, db.ForeignKey("comment.id"))
    comment = db.relationship('Comment')
    bookid = db.Column(db.Integer, db.ForeignKey("book.id"))
    rating = db.Column(db.Integer)
    create_date = db.Column(db.DateTime, default=datetime.today())

class AnonymousUser(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))

class AnonymouseImage(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(100))

