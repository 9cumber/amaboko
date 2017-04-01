# encoding: utf8

from urllib2 import HTTPError
from typing import Union
from amazon.api import AmazonAPI, AmazonProduct


class ServiceUnavailableException(Exception):
    pass


class NotFoundException(Exception):
    pass


def normalize_isbn_format(isbn13):
    # type: (str) -> str
    return isbn13.replace("-", "").replace(" ", "")


def is_isbn_validate(isbn13):
    # type: (str) -> bool

    import re
    check_digit = int(isbn13[-1])
    num_filtered = re.search(r'^(\d{12})$', isbn13[:-1])
    if not num_filtered:
        return False

    digits = num_filtered.group(1)

    res = 0
    for i, digit in enumerate(digits):
        res += (1 if (i + 1) % 2 == 1 else 3) * int(digit)

    return True if (10 - res % 10) == check_digit else False


class AmazonBook(object):
    ATTEMPTS = 5

    def __init__(self,
                 access_key,
                 secret_key,
                 associate_tag,
                 primary_region="JP",
                 secondary_region="US"):
        # type: (str, str, str, str, str) -> None

        self.p_amazon = AmazonAPI(
            access_key, secret_key, associate_tag, region=primary_region)
        self.s_amazon = AmazonAPI(
            access_key, secret_key, associate_tag, region=secondary_region)

    def get_amazon(self, use_secondary=False):
        # type: (bool) -> AmazonAPI
        return self.p_amazon if not use_secondary else self.s_amazon

    def single_lookup(self, isbn13, amazon):
        # type: (str, AmazonAPI) -> AmazonProduct
        try:
            return amazon.lookup(
                ItemId=isbn13, IdType="ISBN", SearchIndex="Books")
        except HTTPError as error:
            if error.code == 400:
                raise NotFoundException
            elif error.code == 503:
                raise ServiceUnavailableException
            else:
                raise

    def lookup(self, isbn13):
        # type: (str) -> Union[AmazonProduct, None]
        isbn13 = normalize_isbn_format(isbn13)

        if is_isbn_validate(isbn13) is False:
            return None

        return self._lookup(isbn13)

    def _lookup(self, isbn13):
        # type: (str) -> Union[AmazonProduct, None]
        remained = self.ATTEMPTS
        should_check_secondary = False
        while remained > 0:
            try:
                amazon = self.get_amazon(should_check_secondary)

                book = self.single_lookup(isbn13, amazon)
                if book is not None:
                    return book

            except NotFoundException:
                if not should_check_secondary:
                    should_check_secondary = True
                else:
                    return None

            except ServiceUnavailableException:
                remained = remained - 1
                continue

            else:
                return None
