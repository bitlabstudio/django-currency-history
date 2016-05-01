# -*- encoding: utf-8 -*-
"""
Python setup file for the currency_history app.
In order to register your app at pypi.python.org, create an account at
pypi.python.org and login, then register your new app like so:
    python setup.py register
If your name is still free, you can now make your first release but first you
should check if you are uploading the correct files:
    python setup.py sdist
Inspect the output thoroughly. There shouldn't be any temp files and if your
app includes staticfiles or templates, make sure that they appear in the list.
If something is wrong, you need to edit MANIFEST.in and run the command again.
If all looks good, you can make your first release:
    python setup.py sdist upload
For new releases, you need to bump the version number in
currency_history/__init__.py and re-run the above command.
For more information on creating source distributions, see
http://docs.python.org/2/distutils/sourcedist.html
"""
import os
from setuptools import setup, find_packages
import currency_history as app


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name="django-currency-history",
    version=app.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, currency, currencies, history, money, rates, rate',
    author='Tobias Lorenz',
    author_email='tobias.lorenz@bitmazk.com',
    url="https://github.com/bitmazk/django-currency-history",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django',
        'django-libs',
        'simplejson',
        'requests',
        'beautifulsoup4',
    ],
)
