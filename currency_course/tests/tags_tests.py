"""Tests for the template tags and filters of the currency_course app."""
from django.test import TestCase

from . import factories
from ..templatetags.currency_course_tags import convert_currency


class ConvertCurrencyTestCase(TestCase):
    """Tests for the ``convert_currency`` tag."""
    longMessage = True

    def test_tag(self):
        course = factories.CurrencyCourseFactory()
        result = convert_currency(1, course.from_currency, 'USD').decode()
        self.assertEqual(result, 'n/a', msg='Should return a n/a message.')

        result = convert_currency(
            1, course.from_currency, course.to_currency).decode()
        self.assertEqual(result, 'n/a', msg='Should return a n/a message.')

        factories.CurrencyCourseHistoryFactory(course=course)
        result = convert_currency(1, course.from_currency, course.to_currency)
        self.assertEqual(result, 1.61, msg=(
            'Should return the converted amount.'))
