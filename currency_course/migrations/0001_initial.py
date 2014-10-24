# -*- coding: utf-8 -*-
# flake8: noqa
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Currency'
        db.create_table(u'currency_course_currency', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('iso_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=3)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
        ))
        db.send_create_signal(u'currency_course', ['Currency'])

        # Adding model 'CurrencyCourse'
        db.create_table(u'currency_course_currencycourse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_currency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='courses_from', to=orm['currency_course.Currency'])),
            ('to_currency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='courses_to', to=orm['currency_course.Currency'])),
        ))
        db.send_create_signal(u'currency_course', ['CurrencyCourse'])

        # Adding model 'CurrencyCourseHistory'
        db.create_table(u'currency_course_currencycoursehistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(related_name='history', to=orm['currency_course.CurrencyCourse'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('tracked_by', self.gf('django.db.models.fields.CharField')(default=u'Add your email', max_length=512)),
        ))
        db.send_create_signal(u'currency_course', ['CurrencyCourseHistory'])


    def backwards(self, orm):
        # Deleting model 'Currency'
        db.delete_table(u'currency_course_currency')

        # Deleting model 'CurrencyCourse'
        db.delete_table(u'currency_course_currencycourse')

        # Deleting model 'CurrencyCourseHistory'
        db.delete_table(u'currency_course_currencycoursehistory')


    models = {
        u'currency_course.currency': {
            'Meta': {'ordering': "['iso_code']", 'object_name': 'Currency'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'currency_course.currencycourse': {
            'Meta': {'ordering': "['from_currency__iso_code', 'to_currency__iso_code']", 'object_name': 'CurrencyCourse'},
            'from_currency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'courses_from'", 'to': u"orm['currency_course.Currency']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_currency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'courses_to'", 'to': u"orm['currency_course.Currency']"})
        },
        u'currency_course.currencycoursehistory': {
            'Meta': {'ordering': "['-date', 'course__to_currency__iso_code']", 'object_name': 'CurrencyCourseHistory'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'history'", 'to': u"orm['currency_course.CurrencyCourse']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tracked_by': ('django.db.models.fields.CharField', [], {'default': "u'Add your email'", 'max_length': '512'}),
            'value': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['currency_course']