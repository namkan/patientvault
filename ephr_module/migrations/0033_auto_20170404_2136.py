# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0032_auto_20170404_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pvprescriptiondetails',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='pvprescriptiondetails',
            name='drug_id',
        ),
        migrations.RemoveField(
            model_name='pvprescriptiondetails',
            name='drug_type',
        ),
        migrations.RemoveField(
            model_name='pvprescriptiondetails',
            name='generic_id',
        ),
        migrations.RemoveField(
            model_name='pvprescriptiondetails',
            name='patient_id',
        ),
        migrations.RemoveField(
            model_name='pvprescriptiondetails',
            name='prescription_id',
        ),
        migrations.RemoveField(
            model_name='pvprescriptiondetails',
            name='strenght_id',
        ),
        migrations.DeleteModel(
            name='PvPrescriptionDetails',
        ),
    ]
