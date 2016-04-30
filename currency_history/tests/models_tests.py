"""Tests for the models of the currency_history app."""
from django.test import TestCase

from mixer.backend.django import mixer


class CurrencyTestCase(TestCase):
    """Tests for the ``Currency`` model."""
    def setUp(self):
        self.currency = mixer.blend('currency_history.Currency')

    def test_model(self):
        self.assertTrue(str(self.currency))


class CurrencyRateTestCase(TestCase):
    """Tests for the ``CurrencyRate`` model."""
    def setUp(self):
        self.rate = mixer.blend('currency_history.CurrencyRate')

    def test_model(self):
        self.assertTrue(str(self.rate))

    def test_latest(self):
        self.assertIsNone(self.rate.latest())


class CurrencyRateHistoryTestCase(TestCase):
    """Tests for the ``CurrencyRateHistory`` model."""
    def setUp(self):
        self.history = mixer.blend('currency_history.CurrencyRateHistory')

    def test_model(self):
        self.assertTrue(str(self.history))
