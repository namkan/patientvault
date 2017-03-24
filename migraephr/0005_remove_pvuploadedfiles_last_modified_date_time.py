# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0004_pvuploadedfiles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pvuploadedfiles',
            name='last_modified_date_time',
        ),
    ]
