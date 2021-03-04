from flask import Blueprint, redirect, request, url_for, render_template, flash
from elice_library import db
from .models import Book, Rental
from datetime import date
from flask_login import current_user, login_required
bp = Blueprint("rental", __name__)

@bp.route("/rental", methods=('POST', 'GET'))
@login_required
def rentalBook():

    bookid = request.form.get("bookid")
    book = Book.query.filter(Book.id == bookid).first()
    userid = current_user.get_id()
    existing_rental = Rental.query.filter(Rental.userid == userid, Rental.bookid == bookid, Rental.return_date == None).first()

    if book.quantity < 1:
        flash("모든 책이 대출되었습니다.", category="alert")

    elif existing_rental:
        flash("이미 대여한 책입니다.", category="alert")

    else:
        new_rental = Rental(userid=userid, bookid=bookid)
        book.quantity -= 1
        db.session.add(new_rental)
        db.session.commit()
        flash("[%s] 대여 완료" % book.book_name, category="alert")

    return redirect(url_for('book.getAllBook'))


@bp.route('/return', methods=('GET', 'POST'))
@login_required
def return_book():

    userid = current_user.get_id()

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
@login_required
def rental_log():

    userid = current_user.get_id()
    rentals = Rental.query.filter(Rental.userid == userid).order_by(Rental.rental_date.desc()).all()

    return render_template('book/rental_log.html', rentals = rentals)
