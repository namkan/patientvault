# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0039_auto_20170404_2003'),
        ('ephr_module', '0035_remove_pvprescriptiondetails_patient_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvprescriptiondetails',
            name='patient_id',
            field=models.ForeignKey(to='registration.PvUser', null=True, blank=True),
        ),
    ]
