# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0030_auto_20170403_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvuser',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
