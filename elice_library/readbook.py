import csv
from elice_library import db
from models import Book

f = open('booklist.csv', encoding='UTF8')
rdr = csv.reader(f)

for line in rdr:

    book = Book(book_name=line[1], publisher = line[2], author=line[3], publication_date=line[4], pages=line[5], description=line[7], link=line[8], rating=0, isbn=line[6])
    db.session.add(book)
    db.session.commit()

f.close()