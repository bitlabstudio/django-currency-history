# flake8: noqa
# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 01:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso_code', models.CharField(max_length=3, unique=True, verbose_name='ISO-code')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('abbreviation', models.CharField(blank=True, help_text='e.g. \u20ac or $', max_length=10, verbose_name='Abbreviation')),
            ],
            options={
                'ordering': ['iso_code'],
            },
        ),
        migrations.CreateModel(
            name='CurrencyRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates_from', to='currency_history.Currency', verbose_name='From currency')),
                ('to_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates_to', to='currency_history.Currency', verbose_name='To currency')),
            ],
            options={
                'ordering': ['from_currency__iso_code', 'to_currency__iso_code'],
            },
        ),
        migrations.CreateModel(
            name='CurrencyRateHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('value', models.FloatField(help_text='Value of the second currency in relation to the first.', verbose_name='Value')),
                ('tracked_by', models.CharField(default='Add your email', max_length=512, verbose_name='Tracked by')),
                ('rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='currency_history.CurrencyRate', verbose_name='Rate')),
            ],
            options={
                'ordering': ['-date', 'rate__to_currency__iso_code'],
            },
        ),
    ]
