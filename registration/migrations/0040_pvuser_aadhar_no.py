# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0039_auto_20170404_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvuser',
            name='aadhar_no',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
