"""Admin classes for the currency_history app."""
from django.contrib import admin

from . import models


class CurrencyRateHistoryAdmin(admin.ModelAdmin):
    list_display = ['rate', 'value', 'date', 'tracked_by']
    list_filter = ['tracked_by']


admin.site.register(models.Currency)
admin.site.register(models.CurrencyRate)
admin.site.register(models.CurrencyRateHistory, CurrencyRateHistoryAdmin)
