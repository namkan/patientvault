# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0009_pvsocialhistory_tobacoquitdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pvsocialhistory',
            name='patientId',
        ),
    ]
