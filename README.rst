Django Currency Course
======================

A reusable Django app that track currency courses.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-currency-course

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/bitmazk/django-currency-course.git#egg=currency_course

TODO: Describe further installation steps (edit / remove the examples below):

Add ``currency_course`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'currency_course',
    )

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load currency_course_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate currency_course


Usage
-----

First fill the database with currencies and add your desired courses.
By default you will have to track the course history by yourself. Check the
management commands and settings for automated trackings.

Management Commands
-------------------

track_currency_courses
^^^^^^^^^^^^^^^^^^^^^^

Run this command to let external services like Google or Yahoo track currency
rates.

    ./manage.py track_currency_courses

Settings
--------

CURRENCY_SERVICE
^^^^^^^^^^^^^^^^

Default = None

By default no external service tracks your course histories.
The following services are available:

* ``'openexchangerates'``: https://openexchangerates.org/
* more coming soon...


OPENEXCHANGERATES_APP_ID
^^^^^^^^^^^^^^^^^^^^^^^^

Default = False

If you want to make use of the ``openexchangerates`` service, make sure to
register at https://openexchangerates.org/ and provide your App ID.


CURRENCY_EMAIL_REPORT
^^^^^^^^^^^^^^^^^^^^^

Default = False

Enable this settings to receive an email report every time the
``track_currency_courses`` command was called.


Template Tags
-------------

convert_currency
^^^^^^^^^^^^^^^^

Convert an amount from one currency to another using the latest history.

    {% load currency_course_tags %}
    {% convert_currency 2 'EUR' 'SGD' as converted_amount %}


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-currency-course
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch
