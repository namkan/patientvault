# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0022_pvfamilyhistory_familyhistorystatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvfamilyhistory',
            name='activeYesNo',
            field=models.BooleanField(default=False),
        ),
    ]
