# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0010_auto_20170325_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pvreminders',
            name='reminder_date',
        ),
        migrations.AlterField(
            model_name='pvreminders',
            name='status',
            field=models.BigIntegerField(null=True, blank=True, choices=[('active', 1), ('closed', 0)]),
        ),
    ]
