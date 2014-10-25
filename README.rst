Django Currency History
=======================

A reusable Django app that tracks currency rates.

.. image:: https://raw.githubusercontent.com/bitmazk/django-currency-history/master/admin.png

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-currency-history

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/bitmazk/django-currency-history.git#egg=currency_history

TODO: Describe further installation steps (edit / remove the examples below):

Add ``currency_history`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'currency_history',
    )

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load currency_history_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate currency_history


Usage
-----

First fill the database with currencies and add your desired rates.
By default you will have to track the history by yourself. Check the
management commands and settings for automated trackings.

Management Commands
-------------------

track_currency_rates
++++++++++++++++++++

Run this command to let external services like Google or Yahoo track currency
rates.

    ./manage.py track_currency_rates

You might want to run it with a cron job.

Settings
--------

CURRENCY_SERVICE
++++++++++++++++

Default = None

By default no external service tracks your rate histories.
The following services are available:

* ``'openexchangerates'``: https://openexchangerates.org/
* ``'yahoo'``: http://finance.yahoo.com/currency-converter/


OPENEXCHANGERATES_APP_ID
++++++++++++++++++++++++

Default = False

If you want to make use of the ``openexchangerates`` service, make sure to
register at https://openexchangerates.org/ and provide your App ID.


CURRENCY_EMAIL_REPORT
+++++++++++++++++++++

Default = False

Enable this settings to receive an email report every time the
``track_currency_rates`` command was called.


Template Tags
-------------

convert_currency
++++++++++++++++

Convert an amount from one currency to another using the latest history.

    {% load currency_history_tags %}
    {% convert_currency 2 'EUR' 'SGD' as converted_amount %}


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-currency-history
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch
