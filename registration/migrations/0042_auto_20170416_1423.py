# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0041_auto_20170416_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pvfamilyhistory',
            name='sharedYesNo',
        ),
        migrations.RemoveField(
            model_name='pvmedicalhistory',
            name='sharedYesNo',
        ),
        migrations.RemoveField(
            model_name='pvsocialhistory',
            name='sharedYesNo',
        ),
        migrations.RemoveField(
            model_name='pvsurgicalhistory',
            name='sharedYesNo',
        ),
    ]
