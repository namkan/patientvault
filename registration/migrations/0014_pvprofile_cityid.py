# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0013_pvprofile_stateid'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvprofile',
            name='cityId',
            field=models.ForeignKey(to='registration.CityMaster', blank=True, null=True),
        ),
    ]
