# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_remove_pvuser_ptime'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvuser',
            name='pTime',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
