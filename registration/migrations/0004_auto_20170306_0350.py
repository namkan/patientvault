# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20170306_0326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surgicalhistorymaster',
            name='lastModifiedDateTime',
        ),
        migrations.RemoveField(
            model_name='surgicalhistorymaster',
            name='name',
        ),
    ]
