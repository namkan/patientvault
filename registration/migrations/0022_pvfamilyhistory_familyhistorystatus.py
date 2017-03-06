# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0021_remove_pvfamilyhistory_familyhistorystatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvfamilyhistory',
            name='familyhistoryStatus',
            field=models.CharField(null=True, max_length=10, blank=True),
        ),
    ]
