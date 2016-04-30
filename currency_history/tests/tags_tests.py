"""Tests for the template tags and filters of the currency_history app."""
from django.test import TestCase

from mixer.backend.django import mixer

from ..templatetags.currency_history_tags import convert_currency


class ConvertCurrencyTestCase(TestCase):
    """Tests for the ``convert_currency`` tag."""
    longMessage = True

    def test_tag(self):
        rate = mixer.blend('currency_history.CurrencyRate')
        result = convert_currency(1, rate.from_currency, 'USD')
        self.assertEqual(result, 'n/a', msg='Should return a n/a message.')

        result = convert_currency(
            1, rate.from_currency, rate.to_currency)
        self.assertEqual(result, 'n/a', msg='Should return a n/a message.')

        mixer.blend('currency_history.CurrencyRateHistory', rate=rate,
                    value=1.61)
        result = convert_currency(1, rate.from_currency, rate.to_currency)
        self.assertEqual(result, 1.61, msg=(
            'Should return the converted amount.'))
