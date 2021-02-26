import csv
import random
from flask import Blueprint, render_template, Response, session, request, redirect, url_for
from elice_library import db
from .models import Book, Comment
from datetime import datetime
from sqlalchemy import func

bp = Blueprint("book", __name__, url_prefix="/book")

@bp.route('/init')
def initBook():


    # f = open('C:\\Users\\swamy\\OneDrive\\Desktop\\elice\\elice_library\\elice_library\\booklist.csv', encoding='UTF8')
    # rdr = csv.reader(f)
    #
    # for line in rdr:
    #     if line[0] == ' ':continue
    #     rate = random.randrange(6)
    #
    #     book = Book(book_name=line[1], publisher=line[2], author=line[3], publication_date=line[4], pages=line[5],
    #                 description=line[7], link=line[8], rating=rate, isbn=line[6])
    #     db.session.add(book)
    #     db.session.commit()
    #
    # f.close()

    with open('C:\\Users\\swamy\\OneDrive\\Desktop\\elice\\elice_library\\elice_library\\booklist.csv', 'r', encoding='UTF8') as f:
        reader = csv.DictReader(f)

        for row in reader:

            print(row)

            image_path = f"\\static\\image\\{row[' ']}"
            try:
                open(f'C:\\Users\\swamy\\OneDrive\\Desktop\\elice\\elice_library\\elice_library{image_path}.png')
                image_path += '.png'
            except:
                image_path += '.jpg'
            image_path = image_path.replace("\\", "/")

            published_at = datetime.strptime(
                row['publication_date'], '%Y-%m-%d').date()
            book = Book(
                # id=int(row['id']),
                book_name=row['book_name'],
                publisher=row['publisher'],
                author=row['author'],
                publication_date=published_at,
                pages=int(row['pages']),
                isbn=row['isbn'],
                description=row['description'],
                image_path=image_path,
                quantity=random.randrange(13),
                rating=random.uniform(1,5),
                link=row['link']
            )
            db.session.add(book)
        db.session.commit()

    return Response(status=200)

@bp.route('/')
def getAllBook():

    books = Book.query.all()

    return render_template('book/main.html', books=books)

@bp.route('/<int:bookid>')
def getBook(bookid):

    book = Book.query.get(bookid)
    comments = Comment.query.filter(Comment.bookid == bookid).order_by(Comment.create_date.desc()).all()
    return render_template('book/info.html', book=book, comments=comments)

@bp.route('/<int:bookid>/comment', methods=["POST"])
def create_comment(bookid):

    userid = session['userid']

    if request.method == "POST":

        content = request.form['content']
        rating = request.values.get('rating')
        comment = Comment(userid=userid, content=content, bookid=bookid, rating = rating)
        db.session.add(comment)
        db.session.commit()

        total, count = db.session\
            .query(func.sum(Comment.rating), func.count(Comment.rating))\
            .filter(Comment.rating != None)\
            .group_by(Comment.bookid)\
            .having( Comment.bookid==bookid)\
            .first()

        new_rating = total / count
        book = Book.query.get(bookid)
        book.rating = new_rating

        db.session.commit()

    return redirect(url_for('book.getBook',bookid=bookid))

