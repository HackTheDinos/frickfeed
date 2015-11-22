# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0002_token_max_lengths'),
        ('records', '0003_date_rec_not_req'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='transcriber',
            field=models.ForeignKey(blank=True, to='socialaccount.SocialAccount', null=True),
        ),
    ]
