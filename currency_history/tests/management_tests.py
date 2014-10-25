"""Tests for the management commands of the ``currency_history`` app."""
from django.core.exceptions import ImproperlyConfigured
from django.core.management import call_command
from django.test import TestCase

from mailer.models import Message

from . import factories
from ..models import CurrencyRateHistory


class TrackCurrencyRatesTestCase(TestCase):
    """Tests for the ``track_currency_rates`` management command."""
    longMessage = True

    def test_command(self):
        call_command('track_currency_rates')
        self.assertEqual(CurrencyRateHistory.objects.count(), 0)

        factories.CurrencyRateFactory(
            from_currency__iso_code='USD',
            to_currency__iso_code='EUR',
        )

        with self.settings(CURRENCY_SERVICE=None):
            with self.assertRaises(ImproperlyConfigured):
                call_command('track_currency_rates')

        call_command('track_currency_rates')
        self.assertEqual(CurrencyRateHistory.objects.count(), 1)
        self.assertEqual(Message.objects.count(), 1)

        with self.settings(CURRENCY_SERVICE='openexchangerates',
                           OPENEXCHANGERATES_APP_ID=None):
            with self.assertRaises(ImproperlyConfigured):
                call_command('track_currency_rates')

        with self.settings(CURRENCY_SERVICE='openexchangerates'):
            # Don't forget to add your App ID to your local settings
            call_command('track_currency_rates')
