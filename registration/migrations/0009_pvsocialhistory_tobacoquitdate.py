# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_remove_pvsocialhistory_tobacoquitdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvsocialhistory',
            name='tobacoQuitDate',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
    ]
