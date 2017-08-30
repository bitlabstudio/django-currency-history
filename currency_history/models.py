"""Models for the currency_history app."""
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Currency(models.Model):
    """
    Contains information about one currency.

    :iso_code: ISO-4217-Code of the currency (e.g. EUR).
    :title: Official title of the currency.
    :abbreviation: Abbreviation of the currency title.

    """
    iso_code = models.CharField(
        verbose_name=_('ISO-code'),
        max_length=3,
        unique=True,
    )

    title = models.CharField(
        verbose_name=_('Title'),
        max_length=50,
    )

    abbreviation = models.CharField(
        verbose_name=_('Abbreviation'),
        max_length=10,
        help_text=_(u'e.g. \u20AC or \u0024'),
        blank=True,
    )

    class Meta:
        ordering = ['iso_code']
        verbose_name = _('Currency')
        verbose_name_plural = _('Currencies')

    def save(self, *args, **kwargs):
        self.iso_code = self.iso_code.upper()
        super(Currency, self).save(*args, **kwargs)

    def __str__(self):
        return self.iso_code


@python_2_unicode_compatible
class CurrencyRate(models.Model):
    """
    Connects two currencies to a rate.

    :from_currency: Currency to convert.
    :to_currency: Currency to be converted to.
    :fixed_rate: Optional fixed rate.

    """
    from_currency = models.ForeignKey(
        Currency,
        verbose_name=_('From currency'),
        related_name='rates_from',
    )

    to_currency = models.ForeignKey(
        Currency,
        verbose_name=_('To currency'),
        related_name='rates_to',
    )

    fixed_rate = models.FloatField(
        verbose_name=_('Fixed rate'),
        blank=True, null=True,
    )

    class Meta:
        ordering = ['from_currency__iso_code', 'to_currency__iso_code']
        verbose_name = _('Currency rate')
        verbose_name_plural = _('Currency rates')

    def __str__(self):
        return u'{} - {}'.format(self.from_currency, self.to_currency)

    def latest(self):
        try:
            return self.history.all()[0]
        except IndexError:
            return None


@python_2_unicode_compatible
class CurrencyRateHistory(models.Model):
    """
    Tracks a rate status.

    :rate: The tracked rate.
    :date: Date the status was tracked.
    :value: Value of the second currency in relation to the first.
    :tracked_by: Field to track a service or user who added the history.

    """
    rate = models.ForeignKey(
        CurrencyRate,
        verbose_name=_('Rate'),
        related_name='history',
    )

    date = models.DateTimeField(
        verbose_name=_('Date'),
        auto_now_add=True,
    )

    value = models.FloatField(
        verbose_name=_('Value'),
        help_text=_('Value of the second currency in relation to the first.'),
    )

    tracked_by = models.CharField(
        max_length=512,
        verbose_name=_('Tracked by'),
        default=_('Add your email'),
    )

    class Meta:
        ordering = ['-date', 'rate__to_currency__iso_code']
        verbose_name = _('Currency rate history')
        verbose_name_plural = _('Currency rate history')

    def __str__(self):
        return u'{} / {}'.format(self.rate, self.date)
