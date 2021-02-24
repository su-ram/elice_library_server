import csv
import random
from flask import Blueprint, render_template, Response, jsonify
from elice_library import db
from .models import Book
from datetime import date, datetime
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
    data = []

    for book in books:

        temp = {}
        temp['id'] = book.id
        temp['book_name'] = book.book_name
        temp['author'] = book.author
        temp['publication_date'] = book.publication_date
        temp['pages'] = book.pages
        temp['link'] = book.link
        temp['rating'] = book.rating
        temp['isbn'] = book.isbn
        temp['publisher'] = book.publisher
        temp['description'] = book.description
        temp['quantity'] = book.quantity
        temp['image_path'] = book.image_path
        data.append(temp)

    return render_template('book/main.html', books=data)

@bp.route('/<bookid>')
def getBook(bookid):

    book = Book.query.get(bookid)

    return render_template('book/info.html', book=book)
