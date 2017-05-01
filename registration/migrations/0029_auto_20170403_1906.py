# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0028_auto_20170403_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvuser',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True, default=0),
        ),
    ]
