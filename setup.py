"""
This file provider the config for PYPI.org
"""

import os

from setuptools import setup

HERE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(HERE, 'README.md'), 'r', encoding='utf8') as f:
    long_description = f.read()
pypi_version = os.getenv('PYPI_VERSION')
if not pypi_version:
    raise RuntimeError("PYPI_VERSION is not installed")
setup(
    name='yasuo',
    version=os.getenv('PYPI_VERSION'),
    description='A Yasuo Python package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Dung BV',
    url='https://github.com/puffer-python/yasuo',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT License',
    keywords='yasuo,python,vietnamese',
    author_email='bvdzung@gmail.com',
    packages=['yasuo'],
    platforms=['Linux (x86, x86_64, ARMv6, ARMv7, ARMv8)',
               'Windows (32-bit, 64-bit)', 'macOS (x86_64)'],
    install_requires=[
        'pytz', 'slugify', 'unidecode'
    ],
)
