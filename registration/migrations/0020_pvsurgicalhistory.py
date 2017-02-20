# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0019_auto_20170220_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='PvSurgicalHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('sharedYesNo', models.BooleanField(default=True)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.DateTimeField()),
                ('patientId', models.OneToOneField(null=True, to='registration.PvUser', blank=True)),
                ('surgicalhistoryId', models.ForeignKey(null=True, to='registration.SurgicalhistoryMaster', blank=True)),
            ],
        ),
    ]
