from elice_library import db
from datetime import datetime

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(30), primary_key=True)
    password = db.Column(db.String(30))

    def __init__(self, name, email, password):
        self.email = email
        self.name = name
        self.password = password

class Book(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_name = db.Column(db.String(100))
    publisher = db.Column(db.String(30))
    author = db.Column(db.String(30))
    publication_date = db.Column(db.DATE)
    pages = db.Column(db.Integer)
    description = db.Column(db.TEXT)
    link = db.Column(db.String(200))
    rating = db.Column(db.FLOAT)
    isbn = db.Column(db.BIGINT)
    quantity = db.Column(db.Integer)
    image_path = db.Column(db.String(50))

    def __init__(self,
                 book_name,
                 publisher,
                 author,
                 publication_date,
                 pages,
                 description,
                 link,
                 rating,
                 isbn,
                 quantity,
                 image_path):


        self.book_name = book_name
        self.publisher = publisher
        self.author = author
        self.publication_date = publication_date
        self.pages = pages
        self.description = description
        self.link = link
        self.rating = rating
        self.isbn = isbn
        self.quantity = quantity
        self.image_path = image_path

class Rental(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.ForeignKey("user.id"))
    bookid = db.Column(db.ForeignKey("book.id"))
    rental_date = db.Column(db.Date, nullable=False, default=datetime.today().date())
    return_date = db.Column(db.Date, nullable=True, default=None)

    def __init__(self, userid, bookid):

        self.userid = userid
        self.bookid = bookid

class BookRental(Book):

    rental_date = None

    def __init__(self, rental_date):

        super()
        self.rental_date = rental_date

