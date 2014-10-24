"""Tests for the models of the currency_course app."""
from django.test import TestCase

from . import factories


class CurrencyTestCase(TestCase):
    """Tests for the ``Currency`` model."""
    def setUp(self):
        self.currency = factories.CurrencyFactory()

    def test_model(self):
        self.assertTrue(self.currency.pk)


class CurrencyCourseTestCase(TestCase):
    """Tests for the ``CurrencyCourse`` model."""
    def setUp(self):
        self.course = factories.CurrencyCourseFactory()

    def test_model(self):
        self.assertTrue(self.course.pk)

    def test_latest(self):
        self.assertIsNone(self.course.latest())


class CurrencyCourseHistoryTestCase(TestCase):
    """Tests for the ``CurrencyCourseHistory`` model."""
    def setUp(self):
        self.history = factories.CurrencyCourseHistoryFactory()

    def test_model(self):
        self.assertTrue(self.history.pk)
