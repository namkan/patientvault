# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0008_pvradorders_patient_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvradorders',
            name='order_status',
            field=models.CharField(null=True, max_length=50, blank=True, choices=[('ordered', 1), ('Inprogress', 2), ('processed', 3)]),
        ),
    ]
