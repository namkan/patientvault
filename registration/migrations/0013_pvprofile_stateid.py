# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0012_pvprofile_countryid'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvprofile',
            name='stateId',
            field=models.ForeignKey(null=True, blank=True, to='registration.StateMaster'),
        ),
    ]
