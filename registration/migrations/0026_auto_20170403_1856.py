# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0025_auto_20170403_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pvuser',
            name='userId',
        ),
        migrations.AddField(
            model_name='pvuser',
            name='id',
            field=models.AutoField(serialize=False, verbose_name='ID', primary_key=True, default=datetime.datetime(2017, 4, 3, 18, 56, 39, 418278, tzinfo=utc), auto_created=True),
            preserve_default=False,
        ),
    ]
