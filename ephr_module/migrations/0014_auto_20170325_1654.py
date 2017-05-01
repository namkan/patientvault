# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0013_auto_20170325_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pvreminders',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='pvreminders',
            name='patient_id',
        ),
    ]
