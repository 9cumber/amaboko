# amaboko - Amazon Book Information API

just wrapping [Amazon Simple Product API](https://github.com/yoavaviram/python-amazon-simple-product-api)

### Dependencies
* Python 2.7.x
* Amazon Product Advertising account (for APIAccessKey, APISecretKey)
* AWS account (for AmazonAssociateTag)

```
$ pip install -r requirements.txt
```

### Description

Choose 2 regions for endpoints, primary and secondary. If specified book information was not found in primary region, instead of that, this module will automatically get the information from secondary region. Of course, you can't necessarily get the information you want.

### Preparation for test

set environment variable **APIAccessKey, APISecretKey, AssocTag**.

```
$ AMAZON_ACCESS_KEY = "APIAccessKey"
$ AMAZON_SECRET_KEY = "APISecretKey"
$ AMAZON_ASSOC_TAG = "AssocTag"
```

or create `test_settings.py`

```
$ vim test_settings.py
```

```
AMAZON_ACCESS_KEY = "APIAccessKey"
AMAZON_SECRET_KEY = "APISecretKey"
AMAZON_ASSOC_TAG = "AssocTag"
```

If you didn't do above both of the above settings, you should pass those variables when you instantiate AmazonBook class. In the case of you imported this module, you have got to pass variables to AmazonBook constructor.

### Usage

You can set primary and secondary regions from `["US", "FR", "CN", "UK", "IN", "CA", "DE", "JP", "IT", "ES"]` in instantiation. (default regions are "JP" and "US")

```
>>> from amabako import AmazonBook, is_isbn_validate
>>> a = AmazonBook()

>>> isbn = "9784048816592"
>>> print is_isbn_validate(isbn)
False

>>> isbn = "9781433551666"
>>> print is_isbn_validate(isbn)
True

>>> book = a.lookup(isbn)

>>> print book.title
Holy Bible: English Standard Version, Value Compact Bible, Trutone Turquoise, Emblem Design

>>> print book.large_image_url
http://ecx.images-amazon.com/images/I/412mbT1AvIL.jpg

>>> print book.get_attribute('Publisher')
Crossway Books

>>> print book.price_and_currency
('1531', 'JPY')
```
