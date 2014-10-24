"""Factories for the currency_course app."""
import factory

from .. import models


class CurrencyFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Currency

    iso_code = factory.Sequence(lambda x: str(100 + x))
    title = factory.Sequence(lambda x: u'Currency{}'.format(x))


class CurrencyCourseFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.CurrencyCourse

    from_currency = factory.SubFactory(CurrencyFactory)
    to_currency = factory.SubFactory(CurrencyFactory)


class CurrencyCourseHistoryFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.CurrencyCourseHistory

    course = factory.SubFactory(CurrencyCourseFactory)
    value = 1.61
