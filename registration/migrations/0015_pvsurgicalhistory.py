# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0014_pvprofile_cityid'),
    ]

    operations = [
        migrations.CreateModel(
            name='PvSurgicalHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('sharedYesNo', models.BooleanField(default=True)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.DateTimeField()),
                ('patientId', models.OneToOneField(to='registration.PvUser', null=True, blank=True)),
                ('surgicalhistoryId', models.ForeignKey(to='registration.SurgicalhistoryMaster', null=True, blank=True)),
            ],
        ),
    ]
