#!/usr/bin/env python

from setuptools import setup

setup(name='rac',
    version="0.1",
    description='RAC module',
    author="Seth Miller",
    author_email='seth@migrantgeek.com',
    url='https://github.com/migrantgeek/python-rac',
    py_modules=['rac',],
    scripts=['bin/racadm'],
    test_suite='tests',
    keywords = ['dell', 'rac', 'drac']
)
