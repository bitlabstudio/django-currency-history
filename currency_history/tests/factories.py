"""Factories for the currency_history app."""
import factory

from .. import models


class CurrencyFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Currency

    iso_code = factory.Sequence(lambda x: str(100 + x))
    title = factory.Sequence(lambda x: u'Currency{}'.format(x))


class CurrencyRateFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.CurrencyRate

    from_currency = factory.SubFactory(CurrencyFactory)
    to_currency = factory.SubFactory(CurrencyFactory)


class CurrencyRateHistoryFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.CurrencyRateHistory

    rate = factory.SubFactory(CurrencyRateFactory)
    value = 1.61
