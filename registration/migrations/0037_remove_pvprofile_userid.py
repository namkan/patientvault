# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0036_pvuser_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pvprofile',
            name='userId',
        ),
    ]
