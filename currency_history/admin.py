"""Admin classes for the currency_history app."""
from django.contrib import admin

from . import models


class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = ['from_currency', 'to_currency', 'fixed_rate']


class CurrencyRateHistoryAdmin(admin.ModelAdmin):
    list_display = ['rate', 'value', 'date', 'tracked_by']
    list_filter = ['tracked_by']


admin.site.register(models.Currency)
admin.site.register(models.CurrencyRate, CurrencyRateAdmin)
admin.site.register(models.CurrencyRateHistory, CurrencyRateHistoryAdmin)
