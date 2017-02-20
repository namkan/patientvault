# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0021_auto_20170220_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CountryMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StateMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.CharField(max_length=50)),
                ('country', models.ForeignKey(to='registration.CountryMaster')),
            ],
        ),
        migrations.AddField(
            model_name='citymaster',
            name='state',
            field=models.ForeignKey(to='registration.StateMaster'),
        ),
    ]
