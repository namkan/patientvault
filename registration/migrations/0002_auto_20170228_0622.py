# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citymaster',
            name='lastModifiedDateTime',
            field=models.CharField(max_length=50),
        ),
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
        migrations.AlterField(
            model_name='familyhistorymaster',
            name='lastModifiedDateTime',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='gendermaster',
            name='lastModifiedDateTime',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='medicalhistorymaster',
            name='lastModifiedDateTime',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='relationshipmaster',
            name='lastModifiedDateTime',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='statemaster',
            name='lastModifiedDateTime',
            field=models.CharField(max_length=50),
        ),
    ]
