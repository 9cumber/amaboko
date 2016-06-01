# encoding: utf-8

from amazon.api import AmazonAPI
import bottlenose.api
import re
import config as CONFIG



class AmazonBook:

    def __init__(self):
        self.p_book = AmazonAPI(CONFIG.AMAZON_ACCESS_KEY,
                CONFIG.AMAZON_SECRET_KEY,
                CONFIG.AMAZON_ASSOCIATE_TAG,
                region=CONFIG.PRIMARY_REGION)
        self.s_book = AmazonAPI(CONFIG.AMAZON_ACCESS_KEY,
                CONFIG.AMAZON_SECRET_KEY,
                CONFIG.AMAZON_ASSOCIATE_TAG,
                region=CONFIG.SECONDARY_REGION)

    def lookup(self, isbn13):
        if self.isbn_validation(self.isbn_format(isbn13)) == False:
            return None
        isbn13 = self.isbn_format(isbn13)

    def isbn_format(self, isbn13):
        isbn13 = isbn13.replace("-", "").replace(" ", "")
        return isbn13

    def isbn_validation(self, isbn13):
        isbn13 = self.isbn_format(isbn13)
        check_digit = int(isbn13[-1])
        num_filtered = re.search(r'^(\d{12})$', isbn13[:-1])
        if not num_filtered:
            return False

        digits = num_filtered.group(1)

        res = 0
        for i, digit in enumerate(digits):
            res += (1 if (i+1)%2 == 1 else 3) * int(digit)

        return True if (10 - res%10) == check_digit else False
