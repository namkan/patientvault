# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0017_auto_20170213_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citymaster',
            name='state',
        ),
        migrations.RemoveField(
            model_name='statemaster',
            name='country',
        ),
        migrations.RemoveField(
            model_name='pvprofile',
            name='cityId',
        ),
        migrations.RemoveField(
            model_name='pvprofile',
            name='countryId',
        ),
        migrations.RemoveField(
            model_name='pvprofile',
            name='stateId',
        ),
        migrations.DeleteModel(
            name='CityMaster',
        ),
        migrations.DeleteModel(
            name='CountryMaster',
        ),
        migrations.DeleteModel(
            name='StateMaster',
        ),
    ]
