# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0034_pvprescriptiondetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pvprescriptiondetails',
            name='patient_id',
        ),
    ]
