# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0033_haha_tis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='haha',
            name='tis',
        ),
    ]
