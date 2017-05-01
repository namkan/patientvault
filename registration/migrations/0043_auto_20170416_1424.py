# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0042_auto_20170416_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvfamilyhistory',
            name='sharedYesNo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pvmedicalhistory',
            name='sharedYesNo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pvsocialhistory',
            name='sharedYesNo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pvsurgicalhistory',
            name='sharedYesNo',
            field=models.BooleanField(default=True),
        ),
    ]
