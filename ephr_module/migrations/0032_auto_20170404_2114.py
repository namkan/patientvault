# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0031_auto_20170404_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvproblemlist',
            name='freetext_desc',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pvproblemlist',
            name='freetext_yesno',
            field=models.CharField(max_length=100, choices=[('yes', 1), ('no', 0)], blank=True, null=True),
        ),
    ]
