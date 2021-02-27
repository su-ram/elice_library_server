from flask import Blueprint, redirect, request, session, url_for, render_template, flash
from elice_library import db
from .models import Book, Rental
from datetime import date
bp = Blueprint("rental", __name__)

@bp.route("/rental", methods=('POST', 'GET'))
def rentalBook():

    bookid = request.form.get("bookid")
    book = Book.query.filter(Book.id == bookid).first()
    userid = session['userid']

    if book.quantity < 1:
        flash("모든 책이 대출되었습니다.", category="error")

    else:
        new_rental = Rental(userid=userid, bookid=bookid)
        book.quantity -= 1
        db.session.add(new_rental)
        db.session.commit()

    return redirect(url_for('book.getAllBook'))


@bp.before_request
def login_check():

    if 'userid' not in session.keys():
        return redirect('/')


@bp.route('/return', methods=('GET', 'POST'))
def return_book():

    userid = session['userid']

    if request.method == 'POST':

        rentalid = request.form.get('rentalid')
        rental = Rental.query.filter(Rental.id == rentalid).first()
        rental.return_date = date.today()

        book = Book.query.filter(Book.id == rental.bookid).first()
        book.quantity += 1
        db.session.commit()

    rentals = Rental.query.filter(Rental.userid == userid, Rental.return_date == None).all()

    return render_template('book/return.html', rentals = rentals)

@bp.route('/log')
def rental_log():

    userid = session['userid']
    rentals = Rental.query.filter(Rental.userid == userid).all()


    return render_template('book/rental_log.html', rentals = rentals)
