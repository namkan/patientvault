# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_remove_pvsocialhistory_drugdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvsocialhistory',
            name='drugDetails',
            field=models.CharField(blank=True, null=True, max_length=250),
        ),
        migrations.AddField(
            model_name='pvsocialhistory',
            name='drugQuitDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
