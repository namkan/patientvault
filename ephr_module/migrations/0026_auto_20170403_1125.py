# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0025_auto_20170403_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvallergy',
            name='created_by_doc',
            field=models.CharField(max_length=50, blank=True, choices=[('yes', 1), ('no', 0)], null=True),
        ),
        migrations.AlterField(
            model_name='pvallergy',
            name='is_sharable',
            field=models.BooleanField(default=True),
        ),
    ]
