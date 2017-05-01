# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0027_auto_20170403_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvuser',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True),
        ),
    ]
