# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0012_pvreminders_reminder_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvreminders',
            name='status',
            field=models.CharField(blank=True, max_length=15, null=True, choices=[('active', 1), ('closed', 0)]),
        ),
    ]
