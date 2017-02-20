# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0018_auto_20170219_1322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pvsurgicalhistory',
            name='patientId',
        ),
        migrations.RemoveField(
            model_name='pvsurgicalhistory',
            name='surgicalhistoryId',
        ),
        migrations.DeleteModel(
            name='PvSurgicalHistory',
        ),
    ]
