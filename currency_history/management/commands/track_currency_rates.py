from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.management.base import BaseCommand

from django_libs.utils.email import send_email
import requests
from simplejson import loads

from ... import models


class Command(BaseCommand):
    def handle(self, **options):
        rates = models.CurrencyRate.objects.all()
        if not rates:
            print('No rates to track.')
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
            response = requests.get(url)
            result = loads(response.content)
            for rate in rates:
                # Base rate is always USD
                output_currency_to_usd = 1 / result['rates'][
                    rate.from_currency.iso_code]
                usd_to_input_currency = result['rates'][
                    rate.to_currency.iso_code]
                models.CurrencyRateHistory.objects.create(
                    rate=rate,
                    value=output_currency_to_usd * usd_to_input_currency,
                    tracked_by='openexchangerates.org',
                )
            print('{} rate(s) tracked using "openexchangerates.org".'.format(
                rates.count()))
        elif settings.CURRENCY_SERVICE == 'yahoo':
            for rate in rates:
                url = ('https://query.yahooapis.com/v1/public/yql?q=select'
                       '%20*%20from%20yahoo.finance.xchange%20where%20pair'
                       '%20in%20(%22{}{}%22)&format=json&env=store%3A%2F%2F'
                       'datatables.org%2Falltableswithkeys&callback='.format(
                           rate.from_currency.iso_code,
                           rate.to_currency.iso_code))
                response = requests.get(url)
                result = loads(response.content)
                models.CurrencyRateHistory.objects.create(
                    rate=rate,
                    value=result['query']['results']['rate']['Rate'],
                    tracked_by='query.yahooapis.com',
                )
            print('{} rate(s) tracked using "query.yahooapis.com".'.format(
                rates.count()))
        if getattr(settings, 'CURRENCY_EMAIL_REPORT', False):
            send_email(
                None,
                {
                    'rates': rates,
                },
                'currency_history/email/currency_email_report_subject.txt',
                'currency_history/email/currency_email_report_body.html',
                settings.FROM_EMAIL,
                [x[1] for x in settings.MANAGERS],
            )
            print('Email report sent.')
