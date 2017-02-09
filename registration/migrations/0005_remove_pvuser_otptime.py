# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20170208_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pvuser',
            name='otpTime',
        ),
    ]
