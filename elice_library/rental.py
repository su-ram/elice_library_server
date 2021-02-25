from flask import Blueprint, redirect, request, session, url_for
from elice_library import db
from .models import Book, Rental

bp = Blueprint("rental", __name__)

@bp.route("/rental", methods=('POST', 'GET'))
def rentalBook():

    bookid = request.form.get("bookid")
    book = Book.query.filter(Book.id == bookid).first()
    userid = session['isLogin']

    if book.quantity > 0:
        new_rental = Rental(userid = userid, bookid=bookid)
        book.quantity -= 1
        db.session.add(new_rental)
        db.session.commit()

    return redirect(url_for('book.getAllBook'))