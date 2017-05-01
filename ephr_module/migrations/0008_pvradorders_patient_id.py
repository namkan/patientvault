# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0024_auto_20170306_0721'),
        ('ephr_module', '0007_remove_pvradorders_patient_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvradorders',
            name='patient_id',
            field=models.ForeignKey(max_length=100, blank=True, null=True, to='registration.PvUser'),
        ),
    ]
