"""Admin classes for the currency_course app."""
from django.contrib import admin

from . import models


class CurrencyCourseHistoryAdmin(admin.ModelAdmin):
    list_display = ['course', 'value', 'date', 'tracked_by']
    list_filter = ['tracked_by']


admin.site.register(models.Currency)
admin.site.register(models.CurrencyCourse)
admin.site.register(models.CurrencyCourseHistory, CurrencyCourseHistoryAdmin)
