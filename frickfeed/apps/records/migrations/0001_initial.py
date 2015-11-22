# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('location', models.CharField(max_length=10)),
                ('box', models.IntegerField()),
                ('shipping_point', models.CharField(max_length=100)),
                ('collector_name_first', models.CharField(max_length=50)),
                ('collector_name_last', models.CharField(max_length=50)),
                ('date_recorded', models.DateField()),
                ('date', models.DateField()),
                ('season_at', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'record',
            },
        ),
        migrations.CreateModel(
            name='Specimen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('amnh_catalog_a', models.CharField(max_length=10)),
                ('amnh_catalog_b', models.CharField(max_length=10)),
                ('field_no', models.IntegerField()),
                ('description', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=100, null=True)),
                ('record', models.ForeignKey(related_name='specimen', to='records.Record')),
            ],
            options={
                'db_table': 'specimen',
            },
        ),
        migrations.AlterUniqueTogether(
            name='record',
            unique_together=set([('location', 'box')]),
        ),
        migrations.AlterUniqueTogether(
            name='specimen',
            unique_together=set([('record', 'field_no')]),
        ),
    ]
