# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0015_pvsurgicalhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrymaster',
            name='lastModifiedDateTime',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='countrymaster',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
