# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_pvuser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvuser',
            name='mobile_number',
            field=models.IntegerField(unique=True),
        ),
    ]
