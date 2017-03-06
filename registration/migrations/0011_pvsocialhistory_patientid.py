# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0010_remove_pvsocialhistory_patientid'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvsocialhistory',
            name='patientId',
            field=models.OneToOneField(blank=True, to='registration.PvUser', null=True),
        ),
    ]
