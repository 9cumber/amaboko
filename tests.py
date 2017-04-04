# encoding: utf-8

import unittest
from amaboko import AmazonBook, normalize_isbn_format, is_isbn_validate



# follow: https://github.com/yoavaviram/python-amazon-simple-product-api/blob/master/tests.py
_AMAZON_ACCESS_KEY = None
_AMAZON_SECRET_KEY = None
_AMAZON_ASSOC_TAG = None


import os
if 'AMAZON_ACCESS_KEY' in os.environ and 'AMAZON_SECRET_KEY' in os.environ and 'AMAZON_ASSOC_TAG' in os.environ:
    _AMAZON_ACCESS_KEY = os.environ['AMAZON_ACCESS_KEY']
    _AMAZON_SECRET_KEY = os.environ['AMAZON_SECRET_KEY']
    _AMAZON_ASSOC_TAG = os.environ['AMAZON_ASSOC_TAG']

else:
    from test_settings import (AMAZON_ACCESS_KEY,
                               AMAZON_SECRET_KEY,
                               AMAZON_ASSOC_TAG)
    _AMAZON_ACCESS_KEY = AMAZON_ACCESS_KEY
    _AMAZON_SECRET_KEY = AMAZON_SECRET_KEY
    _AMAZON_ASSOC_TAG = AMAZON_ASSOC_TAG





class TestAmazonBook(unittest.TestCase):
    def setUp(self):
        self.amazon = AmazonBook(_AMAZON_ACCESS_KEY, _AMAZON_SECRET_KEY, _AMAZON_ASSOC_TAG)

    def test_lookup(self):
        isbn_list = ["978-4048916592", "978-1433551666", "978-4-04-315101-8"]

        for isbn in isbn_list:
            print "-- This is test for " + isbn
            print "| " + normalize_isbn_format(isbn)
            print "| " + str(is_isbn_validate(isbn))
            kwargs = {"IdType": "ISBN", "SearchIndex": "Books"}
            books = self.amazon.lookup(isbn, **kwargs)
            book = books[0] if isinstance(books, list) else books
            if book is not None:
                print "| " + book.title

if __name__ == '__main__':
    unittest.main()

