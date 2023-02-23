"""
This file provider the config for PYPI.org
"""

import os

from setuptools import setup

HERE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(HERE, 'README.md'), 'r', encoding='utf8') as f:
    long_description = f.read()

setup(
    name='yasuo',
    version='1.0.2',
    description='A Yasuo Python package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Dung BV',
    author_email='bvdzung@gmail.com',
    packages=['yasuo'],
    install_requires=[
        'pytz', 'slugify', 'unidecode'
    ],
)
