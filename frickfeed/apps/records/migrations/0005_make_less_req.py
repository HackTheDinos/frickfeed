# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_record_transcriber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='collector_name_first',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='collector_name_last',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='season_at',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='shipping_point',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
