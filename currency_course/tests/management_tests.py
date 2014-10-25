"""Tests for the management commands of the ``currency_course`` app."""
from django.core.exceptions import ImproperlyConfigured
from django.core.management import call_command
from django.test import TestCase

from mailer.models import Message

from . import factories
from ..models import CurrencyCourseHistory


class TrackCurrencyCoursesTestCase(TestCase):
    """Tests for the ``track_currency_courses`` management command."""
    longMessage = True

    def test_command(self):
        call_command('track_currency_courses')
        self.assertEqual(CurrencyCourseHistory.objects.count(), 0)

        factories.CurrencyCourseFactory(
            from_currency__iso_code='USD',
            to_currency__iso_code='EUR',
        )

        with self.settings(CURRENCY_SERVICE=None):
            with self.assertRaises(ImproperlyConfigured):
                call_command('track_currency_courses')

        call_command('track_currency_courses')
        self.assertEqual(CurrencyCourseHistory.objects.count(), 1)
        self.assertEqual(Message.objects.count(), 1)

        with self.settings(CURRENCY_SERVICE='openexchangerates',
                           OPENEXCHANGERATES_APP_ID=None):
            with self.assertRaises(ImproperlyConfigured):
                call_command('track_currency_courses')

        with self.settings(CURRENCY_SERVICE='openexchangerates'):
            # Don't forget to add your App ID to your local settings
            call_command('track_currency_courses')
