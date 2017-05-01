# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0022_auto_20170402_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugmaster',
            name='last_modified_by',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='drugmaster',
            name='last_modified_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
