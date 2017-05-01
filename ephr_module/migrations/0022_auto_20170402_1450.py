# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0021_pvprescriptiondetails_patient_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvprescription',
            name='shared_yesno',
            field=models.BooleanField(default=True),
        ),
    ]
