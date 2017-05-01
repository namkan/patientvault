# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0017_pvlaborders_order_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvradorders',
            name='order_name',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
