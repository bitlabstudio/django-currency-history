# flake8: noqa
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Currency'
        db.create_table(u'currency_history_currency', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('iso_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=3)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
        ))
        db.send_create_signal(u'currency_history', ['Currency'])

        # Adding model 'CurrencyRate'
        db.create_table(u'currency_history_currencyrate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_currency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rates_from', to=orm['currency_history.Currency'])),
            ('to_currency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rates_to', to=orm['currency_history.Currency'])),
        ))
        db.send_create_signal(u'currency_history', ['CurrencyRate'])

        # Adding model 'CurrencyRateHistory'
        db.create_table(u'currency_history_currencyratehistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rate', self.gf('django.db.models.fields.related.ForeignKey')(related_name='history', to=orm['currency_history.CurrencyRate'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('tracked_by', self.gf('django.db.models.fields.CharField')(default=u'Add your email', max_length=512)),
        ))
        db.send_create_signal(u'currency_history', ['CurrencyRateHistory'])


    def backwards(self, orm):
        # Deleting model 'Currency'
        db.delete_table(u'currency_history_currency')

        # Deleting model 'CurrencyRate'
        db.delete_table(u'currency_history_currencyrate')

        # Deleting model 'CurrencyRateHistory'
        db.delete_table(u'currency_history_currencyratehistory')


    models = {
        u'currency_history.currency': {
            'Meta': {'ordering': "['iso_code']", 'object_name': 'Currency'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'currency_history.currencyrate': {
            'Meta': {'ordering': "['from_currency__iso_code', 'to_currency__iso_code']", 'object_name': 'CurrencyRate'},
            'from_currency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rates_from'", 'to': u"orm['currency_history.Currency']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_currency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rates_to'", 'to': u"orm['currency_history.Currency']"})
        },
        u'currency_history.currencyratehistory': {
            'Meta': {'ordering': "['-date', 'rate__to_currency__iso_code']", 'object_name': 'CurrencyRateHistory'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rate': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'history'", 'to': u"orm['currency_history.CurrencyRate']"}),
            'tracked_by': ('django.db.models.fields.CharField', [], {'default': "u'Add your email'", 'max_length': '512'}),
            'value': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['currency_history']
