# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0005_pvlaborders_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvlaborders',
            name='order_status',
            field=models.CharField(blank=True, null=True, choices=[('ordered', 1), ('Inprogress', 2), ('processed', 3)], max_length=50),
        ),
    ]
