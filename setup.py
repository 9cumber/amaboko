from setuptools import setup

import os

long_description = None
if os.path.exists('README.md'):
    long_description = open('README.md').read()


setup(
    name='amaboko',
    version='0.0.2',
    description='get book information by ISBN in some regions',
    long_description=long_description,
    license="MIT",
    keywords="amazon",
    author='9cumber team',
    author_email='micfall.romtin@gmail.com',
    url='https://github.com/9cumber/amaboko',
    packages=['amaboko'],
    install_requires=['typing', 'python-amazon-simple-product-api'])
