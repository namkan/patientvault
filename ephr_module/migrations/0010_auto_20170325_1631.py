# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0009_auto_20170325_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvreminders',
            name='content',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pvreminders',
            name='reminder_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pvreminders',
            name='status',
            field=models.CharField(blank=True, null=True, max_length=200, choices=[('active', 1), ('closed', 0)]),
        ),
    ]
