# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0024_auto_20170306_0721'),
        ('ephr_module', '0020_auto_20170402_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvprescriptiondetails',
            name='patient_id',
            field=models.ForeignKey(null=True, to='registration.PvUser', blank=True),
        ),
    ]
