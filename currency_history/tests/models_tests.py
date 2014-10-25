"""Tests for the models of the currency_history app."""
from django.test import TestCase

from . import factories


class CurrencyTestCase(TestCase):
    """Tests for the ``Currency`` model."""
    def setUp(self):
        self.currency = factories.CurrencyFactory()

    def test_model(self):
        self.assertTrue(self.currency.pk)


class CurrencyRateTestCase(TestCase):
    """Tests for the ``CurrencyRate`` model."""
    def setUp(self):
        self.rate = factories.CurrencyRateFactory()

    def test_model(self):
        self.assertTrue(self.rate.pk)

    def test_latest(self):
        self.assertIsNone(self.rate.latest())


class CurrencyRateHistoryTestCase(TestCase):
    """Tests for the ``CurrencyRateHistory`` model."""
    def setUp(self):
        self.history = factories.CurrencyRateHistoryFactory()

    def test_model(self):
        self.assertTrue(self.history.pk)
