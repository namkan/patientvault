# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0018_auto_20170306_0526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pvfamilyhistory',
            name='familyhistoryStatus',
        ),
    ]
