# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0017_pvfamilyhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvfamilyhistory',
            name='familyhistoryStatus',
            field=models.IntegerField(default=1),
        ),
    ]
