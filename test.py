# encoding: utf-8

import api

isbn_list = ["978-4048916592", "978-1433551666", "978-4-04-315101-8"]

ama_book = api.AmazonBook()

for isbn in isbn_list:
    print "-- This is test for " + isbn
    print "| " + ama_book.isbn_format(isbn)
    print "| " + str(ama_book.isbn_validation(isbn))
    books = ama_book.lookup(isbn)
    book = books[0] if isinstance(books, list) else books
    if book is not None:
        print "| " + book.title
        print "| " + book.price_and_currency[0]
