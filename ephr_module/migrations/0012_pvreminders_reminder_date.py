# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0011_auto_20170325_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvreminders',
            name='reminder_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
