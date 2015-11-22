# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_specimen_location_not_req'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='date_recorded',
            field=models.DateField(null=True, blank=True),
        ),
    ]
