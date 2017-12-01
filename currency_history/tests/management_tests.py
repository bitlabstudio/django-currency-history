"""Tests for the management commands of the ``currency_history`` app."""
from django.core.exceptions import ImproperlyConfigured
from django.core.management import call_command
from django.test import TestCase

from mixer.backend.django import mixer
from mock import patch
from requests.models import Response

from ..models import CurrencyRateHistory


class TrackCurrencyRatesTestCase(TestCase):
    """Tests for the ``track_currency_rates`` management command."""
    longMessage = True

    @patch('requests.get')
    def test_command(self, mock):
        resp = Response()
        resp._content = (
            '{"base": "USD","date": "2017-08-29","rates": {"EUR": 0.83001}}')
        mock.return_value = resp

        call_command('track_currency_rates')
        self.assertEqual(CurrencyRateHistory.objects.count(), 0)

        eur = mixer.blend('currency_history.Currency', iso_code='EUR')
        usd = mixer.blend('currency_history.Currency', iso_code='USD')
        sgd = mixer.blend('currency_history.Currency', iso_code='SGD')
        rate = mixer.blend('currency_history.CurrencyRate',
                           from_currency=usd, to_currency=eur)

        with self.settings(CURRENCY_SERVICE=None):
            with self.assertRaises(ImproperlyConfigured):
                call_command('track_currency_rates')

        call_command('track_currency_rates')
        self.assertEqual(CurrencyRateHistory.objects.count(), 1)

        resp._content = (
            '{\n  "disclaimer": "Exchange rates provided for informational'
            ' purposes only and do not constitute financial advice of any'
            ' kind. Although every attempt is made to ensure quality, no'
            ' guarantees are made of accuracy, validity, availability, or'
            ' fitness for any purpose. All usage subject to acceptance of'
            ' Terms: https://openexchangerates.org/terms/",\n  "license":'
            ' "Data sourced from various providers; resale prohibited; no'
            ' warranties given of any kind. All usage subject to License'
            ' Agreement: https://openexchangerates.org/license/",\n'
            '  "timestamp": 1461996002,\n  "base": "USD",\n  "rates":'
            ' {\n    "AED": 3.672902,\n    "AFN": 68.39,\n'
            '    "ALL": 121.2507,\n    "AMD": 479.352502,\n'
            '    "ANG": 1.78875,\n    "AOA": 165.780834,\n'
            '    "ARS": 14.28566,\n    "AUD": 1.314714,\n'
            '    "AWG": 1.793333,\n    "AZN": 1.504525,\n'
            '    "BAM": 1.709893,\n    "BBD": 2,\n    "BDT": 78.415719,\n'
            '    "BGN": 1.710583,\n    "BHD": 0.376986,\n'
            '    "BIF": 1559.0225,\n    "BMD": 1,\n    "BND": 1.342811,\n'
            '    "BOB": 6.91409,\n    "BRL": 3.443202,\n    "BSD": 1,\n'
            '    "BTC": 0.002205353717,\n    "BTN": 66.367317,\n'
            '    "BWP": 10.608913,\n    "BYR": 19243.525,\n'
            '    "BZD": 2.002099,\n    "CAD": 1.255009,\n    "CDF": 928.505,\n'
            '    "CHF": 0.960279,\n    "CLF": 0.024602,\n'
            '    "CLP": 660.975806,\n    "CNY": 6.475936,\n'
            '    "COP": 2865.675,\n    "CRC": 536.56,\n    "CUC": 1,\n'
            '    "CUP": 1.000075,\n    "CVE": 96.545983,\n'
            '    "CZK": 23.63836,\n    "DJF": 177.762127,\n'
            '    "DKK": 6.506336,\n    "DOP": 45.81815,\n'
            '    "DZD": 109.1102,\n    "EEK": 13.6941,\n    "EGP": 8.880895,\n'
            '    "ERN": 15.0015,\n    "ETB": 21.59736,\n    "EUR": 0.873433,\n'
            '    "FJD": 2.06495,\n    "FKP": 0.684418,\n    "GBP": 0.684418,\n'
            '    "GEL": 2.226475,\n    "GGP": 0.684418,\n'
            '    "GHS": 3.799722,\n    "GIP": 0.684418,\n'
            '    "GMD": 42.62952,\n    "GNF": 7550.350098,\n'
            '    "GTQ": 7.735843,\n    "GYD": 205.668984,\n'
            '    "HKD": 7.757367,\n    "HNL": 22.56735,\n'
            '    "HRK": 6.562154,\n    "HTG": 62.276388,\n'
            '    "HUF": 272.887002,\n    "IDR": 13190.033333,\n'
            '    "ILS": 3.741807,\n    "IMP": 0.684418,\n'
            '    "INR": 66.42346,\n    "IQD": 1107.210686,\n'
            '    "IRR": 30251.5,\n    "ISK": 122.6744,\n'
            '    "JEP": 0.684418,\n    "JMD": 122.96119,\n'
            '    "JOD": 0.70843,\n    "JPY": 106.584101,\n'
            '    "KES": 101.053031,\n    "KGS": 68.469999,\n'
            '    "KHR": 4044.024976,\n    "KMF": 432.36665,\n'
            '    "KPW": 899.91,\n    "KRW": 1141.89834,\n'
            '    "KWD": 0.30153,\n    "KYD": 0.824297,\n'
            '    "KZT": 327.596391,\n    "LAK": 8110.452598,\n'
            '    "LBP": 1509.468317,\n    "LKR": 145.8947,\n'
            '    "LRD": 90.49095,\n    "LSL": 14.22722,\n'
            '    "LTL": 3.01471,\n    "LVL": 0.61692,\n    "LYD": 1.337591,\n'
            '    "MAD": 9.604217,\n    "MDL": 19.71772,\n'
            '    "MGA": 3184.768317,\n    "MKD": 54.78961,\n'
            '    "MMK": 1170.327451,\n    "MNT": 2011.5,\n'
            '    "MOP": 7.988744,\n    "MRO": 346.176165,\n'
            '    "MTL": 0.683738,\n    "MUR": 35.059275,\n    "MVR": 15.29,\n'
            '    "MWK": 682.459282,\n    "MXN": 17.18277,\n'
            '    "MYR": 3.914682,\n    "MZN": 53.28,\n    "NAD": 14.22922,\n'
            '    "NGN": 199.055601,\n    "NIO": 28.37929,\n'
            '    "NOK": 8.061401,\n    "NPR": 106.1412,\n'
            '    "NZD": 1.432944,\n    "OMR": 0.385056,\n    "PAB": 1,\n'
            '    "PEN": 3.281727,\n    "PGK": 3.149975,\n'
            '    "PHP": 46.99978,\n    "PKR": 104.7959,\n'
            '    "PLN": 3.824367,\n    "PYG": 5565.14,\n    "QAR": 3.640106,\n'
            '    "RON": 3.914786,\n    "RSD": 107.06572,\n'
            '    "RUB": 64.85702,\n    "RWF": 753.957374,\n'
            '    "SAR": 3.750779,\n    "SBD": 7.882966,\n'
            '    "SCR": 13.53356,\n    "SDG": 6.090584,\n    "SEK": 8.03663,\n'
            '    "SGD": 1.344235,\n    "SHP": 0.684418,\n    "SLL": 3946.75,\n'
            '    "SOS": 606.424253,\n    "SRD": 5.5635,\n'
            '    "STD": 21335.45,\n    "SVC": 8.748053,\n'
            '    "SYP": 219.538998,\n    "SZL": 14.21873,\n'
            '    "THB": 34.91862,\n    "TJS": 7.8697,\n    "TMT": 3.50145,\n'
            '    "TND": 2.004954,\n    "TOP": 2.231516,\n'
            '    "TRY": 2.797716,\n    "TTD": 6.647861,\n'
            '    "TWD": 32.27552,\n    "TZS": 2187.766667,\n'
            '    "UAH": 25.185,\n    "UGX": 3321.333317,\n    "USD": 1,\n'
            '    "UYU": 31.75714,\n    "UZS": 2904.625,\n'
            '    "VEF": 9.971618,\n    "VND": 22295.95,\n'
            '    "VUV": 107.923333,\n    "WST": 2.515718,\n'
            '    "XAF": 574.139899,\n    "XAG": 0.0561375,\n'
            '    "XAU": 0.000776,\n    "XCD": 2.70302,\n    "XDR": 0.704801,\n'
            '    "XOF": 579.233339,\n    "XPD": 0.001593,\n'
            '    "XPF": 104.506175,\n    "XPT": 0.000928,\n'
            '    "YER": 249.939,\n    "ZAR": 14.22839,\n'
            '    "ZMK": 5252.024745,\n    "ZMW": 9.583548,\n'
            '    "ZWL": 322.322775\n  }\n}')
        mock.return_value = resp

        with self.settings(CURRENCY_SERVICE='openexchangerates',
                           OPENEXCHANGERATES_APP_ID=None):
            with self.assertRaises(ImproperlyConfigured):
                call_command('track_currency_rates')

        with self.settings(CURRENCY_SERVICE='openexchangerates'):
            # Don't forget to add your App ID to your local settings
            call_command('track_currency_rates')

        with self.settings(CURRENCY_SERVICE='currencylayer'):
            # Don't forget to add your API key to your local settings
            resp._content = (
                '{"success":true,"terms":"https:\\/\\/currencylayer.com\\/'
                'terms","privacy":"https:\\/\\/currencylayer.com\\/privacy",'
                '"timestamp":1512166746,"source":"USD","quotes":{"USDEUR":'
                '0.840204}}')
            mock.return_value = resp
            call_command('track_currency_rates')
            rate.delete()
            rate = mixer.blend('currency_history.CurrencyRate',
                               from_currency=eur, to_currency=usd)
            resp._content = (
                '{"success":true,"terms":"https:\\/\\/currencylayer.com\\/'
                'terms","privacy":"https:\\/\\/currencylayer.com\\/privacy",'
                '"timestamp":1512166746,"source":"USD","quotes":{"USDEUR":'
                '0.840204}}')
            mock.return_value = resp
            call_command('track_currency_rates')
            rate.delete()
            mixer.blend('currency_history.CurrencyRate',
                        from_currency=eur, to_currency=sgd)
            resp._content = (
                '{"success":true,"terms":"https:\\/\\/currencylayer.com\\/'
                'terms","privacy":"https:\\/\\/currencylayer.com\\/privacy",'
                '"timestamp":1512166746,"source":"USD","quotes":{"USDSGD":'
                '1.34555,"USDEUR":0.840204}}')
            mock.return_value = resp
            call_command('track_currency_rates')
