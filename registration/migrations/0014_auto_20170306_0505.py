# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0013_auto_20170306_0502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pvfamilyhisotry',
            name='patientId',
        ),
        migrations.RemoveField(
            model_name='pvfamilyrelationship',
            name='patientId',
        ),
        migrations.RemoveField(
            model_name='pvmedicalhistory',
            name='patientId',
        ),
        migrations.RemoveField(
            model_name='pvprofile',
            name='userId',
        ),
        migrations.RemoveField(
            model_name='pvsocialhistory',
            name='patientId',
        ),
        migrations.RemoveField(
            model_name='pvsurgicalhistory',
            name='patientId',
        ),
    ]
