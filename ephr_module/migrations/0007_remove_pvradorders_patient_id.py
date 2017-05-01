# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0006_auto_20170325_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pvradorders',
            name='patient_id',
        ),
    ]
