# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0015_auto_20170306_0506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pvfamilyhisotry',
            name='familyhistoryId',
        ),
        migrations.RemoveField(
            model_name='pvfamilyhisotry',
            name='patientId',
        ),
        migrations.RemoveField(
            model_name='pvfamilyhisotry',
            name='relationshipId',
        ),
        migrations.DeleteModel(
            name='PvFamilyHisotry',
        ),
    ]
