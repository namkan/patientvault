# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0024_auto_20170306_0721'),
        ('ephr_module', '0014_auto_20170325_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvreminders',
            name='created_by',
            field=models.ForeignKey(to='ephr_module.DpUser', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pvreminders',
            name='patient_id',
            field=models.ForeignKey(to='registration.PvUser', blank=True, null=True),
        ),
    ]
