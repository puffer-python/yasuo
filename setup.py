import os

from setuptools import setup

HERE = os.path.dirname(os.path.abspath(__file__))

long_description = open(os.path.join(HERE, 'README.md'), 'r', encoding='utf8').read()
setup(
    name='yasuo',
    version='1.0.1',
    description='A Yasuo Python package',
    long_description=long_description,
    author='Dung BV',
    author_email='bvdzung@gmail.com',
    packages=['yasuo'],
    install_requires=[
        'pytz', 'slugify', 'unidecode'
    ],
)
