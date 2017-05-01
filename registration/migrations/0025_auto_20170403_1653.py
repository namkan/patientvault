# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0024_auto_20170306_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvprofile',
            name='profilePhoto',
            field=models.URLField(null=True, blank=True),
        ),
    ]
