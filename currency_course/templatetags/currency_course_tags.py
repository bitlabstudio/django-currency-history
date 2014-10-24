from django import template
from django.utils.translation import ugettext_lazy as _

from ..models import CurrencyCourse


register = template.Library()


@register.assignment_tag()
def convert_currency(amount, from_currency, to_currency):
    '''
    Converts currencies.

    Example:
    {% convert_currency 2 'EUR' 'SGD' as amount %}

    '''
    try:
        course = CurrencyCourse.objects.get(
            from_currency__iso_code=from_currency,
            to_currency__iso_code=to_currency)
    except CurrencyCourse.DoesNotExist:
        return _('n/a')
    try:
        history = course.history.all()[0]
    except IndexError:
        return _('n/a')
    return amount * history.value
