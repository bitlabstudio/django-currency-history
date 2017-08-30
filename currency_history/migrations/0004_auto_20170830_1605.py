# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency_history', '0003_currencyratehistory_fixed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currencyratehistory',
            name='fixed',
        ),
        migrations.AddField(
            model_name='currencyrate',
            name='fixed_rate',
            field=models.FloatField(blank=True, null=True, verbose_name='Fixed rate'),
        ),
    ]