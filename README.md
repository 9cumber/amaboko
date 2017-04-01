# Amazon Book Information API

just wrapping [Amazon Simple Product API](https://github.com/yoavaviram/python-amazon-simple-product-api)

### Dependencies
* Python 2.7.x (no guarantee for any other versions)
* Amazon Simlpe Product API - pip
* Bottlenose - pip
* dateutil - pip
* Amazon Product Advertising account (for APIAccessKey, APISecretKey)
* AWS account (for AmazonAssociateTag)

### Description

Choose 2 regions for endpoints, primary and secondary. If specified book information was not found in primary region, instead of that, this module will automatically get the information from secondary region. Of course, you can't necessarily get the information you want.

### Usage

**APIAccessKey, APISecretKey, AssocTag are loaded from `config.py`. Please remember to prepare that.**

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
