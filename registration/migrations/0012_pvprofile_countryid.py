# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0011_citymaster'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvprofile',
            name='countryId',
            field=models.ForeignKey(blank=True, to='registration.CountryMaster', null=True),
        ),
    ]
