# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Suportee'
        db.create_table(u'api_suportee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('age', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('birthday', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('location', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('autobiography', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('contactAt', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('findMeAt', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal(u'api', ['Suportee'])

        # Adding M2M table for field supporters on 'Suportee'
        m2m_table_name = db.shorten_name(u'api_suportee_supporters')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suportee', models.ForeignKey(orm[u'api.suportee'], null=False)),
            ('supporter', models.ForeignKey(orm[u'api.supporter'], null=False))
        ))
        db.create_unique(m2m_table_name, ['suportee_id', 'supporter_id'])

        # Adding model 'Supporter'
        db.create_table(u'api_supporter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('age', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'api', ['Supporter'])

        # Adding model 'Goals'
        db.create_table(u'api_goals', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('suportee', self.gf('django.db.models.fields.related.ForeignKey')(related_name='goals', to=orm['api.Suportee'])),
            ('completed', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('dateOfCompletion', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('meansToAchieve', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal(u'api', ['Goals'])

        # Adding model 'Pledge'
        db.create_table(u'api_pledge', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('suportee', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pledges', to=orm['api.Suportee'])),
            ('suporter', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pledges', to=orm['api.Supporter'])),
            ('value', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
        ))
        db.send_create_signal(u'api', ['Pledge'])


    def backwards(self, orm):
        # Deleting model 'Suportee'
        db.delete_table(u'api_suportee')

        # Removing M2M table for field supporters on 'Suportee'
        db.delete_table(db.shorten_name(u'api_suportee_supporters'))

        # Deleting model 'Supporter'
        db.delete_table(u'api_supporter')

        # Deleting model 'Goals'
        db.delete_table(u'api_goals')

        # Deleting model 'Pledge'
        db.delete_table(u'api_pledge')


    models = {
        u'api.goals': {
            'Meta': {'object_name': 'Goals'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'dateOfCompletion': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meansToAchieve': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'suportee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'goals'", 'to': u"orm['api.Suportee']"})
        },
        u'api.pledge': {
            'Meta': {'object_name': 'Pledge'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'suportee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pledges'", 'to': u"orm['api.Suportee']"}),
            'suporter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pledges'", 'to': u"orm['api.Supporter']"}),
            'value': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'})
        },
        u'api.suportee': {
            'Meta': {'object_name': 'Suportee'},
            'age': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'autobiography': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'birthday': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'contactAt': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'findMeAt': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'supporters': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'supportees'", 'symmetrical': 'False', 'to': u"orm['api.Supporter']"})
        },
        u'api.supporter': {
            'Meta': {'object_name': 'Supporter'},
            'age': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['api']