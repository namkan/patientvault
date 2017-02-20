# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0022_auto_20170220_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvprofile',
            name='cityId',
            field=models.ForeignKey(blank=True, null=True, to='registration.CityMaster'),
        ),
        migrations.AddField(
            model_name='pvprofile',
            name='countryId',
            field=models.ForeignKey(blank=True, null=True, to='registration.CountryMaster'),
        ),
        migrations.AddField(
            model_name='pvprofile',
            name='stateId',
            field=models.ForeignKey(blank=True, null=True, to='registration.StateMaster'),
        ),
    ]
