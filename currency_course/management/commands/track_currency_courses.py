from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.management.base import BaseCommand

from django_libs.utils_email import send_email
from simplejson import loads
from urllib2 import urlopen

from ... import models


class Command(BaseCommand):
    def handle(self, **options):
        courses = models.CurrencyCourse.objects.all()
        if not courses:
            print('No courses to track.')
            return
        if not getattr(settings, 'CURRENCY_SERVICE', None):
            raise ImproperlyConfigured('No currency service defined.')
        if settings.CURRENCY_SERVICE == 'openexchangerates':
            app_id = getattr(settings, 'OPENEXCHANGERATES_APP_ID', False)
            if not app_id:
                raise ImproperlyConfigured(
                    'Setting OPENEXCHANGERATES_APP_ID not set.')
            url = 'http://openexchangerates.org/latest.json?app_id={}'.format(
                settings.OPENEXCHANGERATES_APP_ID)
            response = urlopen(url).read()
            result = loads(response)
            for course in courses:
                # Base rate is always USD
                output_currency_to_usd = 1 / result['rates'][
                    course.from_currency.iso_code]
                usd_to_input_currency = result['rates'][
                    course.to_currency.iso_code]
                models.CurrencyCourseHistory.objects.create(
                    course=course,
                    value=output_currency_to_usd * usd_to_input_currency,
                    tracked_by='openexchangerates.org',
                )
            if getattr(settings, 'CURRENCY_EMAIL_REPORT', False):
                send_email(
                    None,
                    {
                        'courses': courses,
                    },
                    'currency_course/email/currency_email_report_subject.txt',
                    'currency_course/email/currency_email_report_body.html',
                    settings.FROM_EMAIL,
                    [x[1] for x in settings.MANAGERS],
                )
                print('Email report sent.')
            print('{} course(s) tracked using "openexchangerates.org".'.format(
                courses.count()))
            return
        raise ImproperlyConfigured('Service misconfigured.')
