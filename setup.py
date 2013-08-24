from setuptools import setup, find_packages
import os

from .shop_digitalproducts import (
    __package__,
    __version__,
    __license__,
    __author__,
    __author_email__,
    __contributors__,
    __homepage__,
)


setup(
    name=__package__,
    version=__version__,
    packages=find_packages(),
    install_requires=['django-shop',
                      'django-sendfile',
                      'django-classytags',
                      'surlex',
                      ],
    author=__author__,
    author_email=__author_email__,
    description='Sell digital products with django-shop',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    license=__license__,
    keywords='django-shop, product, digital',
    url=__homepage__,
    include_package_data=True
)