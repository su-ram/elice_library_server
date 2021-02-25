from flask import Blueprint, redirect, request, session, render_template
from . import db
from .models import Book, Rental
from datetime import date

bp = Blueprint("_return", __name__)

@bp.before_request
def login_check():

    if 'isLogin' not in session.keys():
        return redirect('/')


@bp.route('/return', methods=('GET', 'POST'))
def return_book():

    userid = session['isLogin']

    if request.method == 'POST':

        rentalid = request.form.get('rentalid')
        rental = Rental.query.filter(Rental.id == rentalid).first()
        rental.return_date = date.today()
        print(rental.rental_date)
        book = Book.query.filter(Book.id == rental.bookid).first()
        book.quantity += 1
        db.session.commit()

    books = []

    data = db.session.query(Rental.rental_date, Book.book_name, Book.image_path, Rental.id, Book.id).filter(Rental.bookid == Book.id, Rental.userid == userid, Rental.return_date == None).all()

    for d in data:

        temp = {}
        temp['rental_date'] = d[0]
        temp['book_name'] = d[1]
        temp['image_path'] = d[2]
        temp['rentalid'] = d[3]
        temp['bookid'] = d[4]

        books.append(temp)

    return render_template('book/return.html', books = books)