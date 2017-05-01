# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0029_auto_20170404_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvallergy',
            name='created_by_doc',
            field=models.BooleanField(default=False),
        ),
    ]
