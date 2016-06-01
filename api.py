# encoding: utf-8

from amazon.api import AmazonAPI
import bottlenose.api
import urllib2
import re
import config as CONFIG



class AmazonBook:


    def __init__(self):
        self.p_amazon = AmazonAPI(CONFIG.AMAZON_ACCESS_KEY,
                CONFIG.AMAZON_SECRET_KEY,
                CONFIG.AMAZON_ASSOCIATE_TAG,
                region=CONFIG.PRIMARY_REGION)
        self.s_amazon = AmazonAPI(CONFIG.AMAZON_ACCESS_KEY,
                CONFIG.AMAZON_SECRET_KEY,
                CONFIG.AMAZON_ASSOCIATE_TAG,
                region=CONFIG.SECONDARY_REGION)


    def lookup(self, isbn13, step="Primary"):
        if self.isbn_validation(self.isbn_format(isbn13)) == False:
            return None

        isbn13 = self.isbn_format(isbn13)
        remained = CONFIG.ATTEMPTS

        while (remained > 0):
            try:
                if step is "Primary":
                    book = self.p_amazon.lookup(ItemId=isbn13, IdType="ISBN", SearchIndex="Books")
                elif step is "Secondary":
                    book = self.s_amazon.lookup(ItemId=isbn13, IdType="ISBN", SearchIndex="Books")
                return book
            except urllib2.HTTPError, e:
                if e.code == 400:
                    if step is "Primary":
                        return self.lookup(isbn13, "Secondary")
                    else:
                        return None
                elif e.code == 503:
                    if remained == 0:
                        return None
                    else:
                        remained = remained - 1
                        continue
                else:
                    return None


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
