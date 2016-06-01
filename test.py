# encoding: utf-8

import api

isbn_list = ["978-4-00-310101-8", "978-4-10-109205-8", "978-4-04-315101-8"]

ama_book = api.AmazonBook()

for isbn in isbn_list:
    print "This is test for " + isbn
    print "| " + ama_book.isbn_format(isbn)
    print "| " + str(ama_book.isbn_validation(isbn))
