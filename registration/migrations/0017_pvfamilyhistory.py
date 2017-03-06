# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0016_auto_20170306_0509'),
    ]

    operations = [
        migrations.CreateModel(
            name='PvFamilyHistory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('familyhistoryStatus', models.BooleanField(default=True)),
                ('sharedYesNo', models.BooleanField(default=True)),
                ('activeYesNo', models.BooleanField()),
                ('lastModifiedDateTime', models.DateTimeField(auto_now_add=True, null=True)),
                ('familyhistoryId', models.ForeignKey(to='registration.FamilyhistoryMaster')),
                ('patientId', models.ForeignKey(blank=True, to='registration.PvUser', null=True)),
                ('relationshipId', models.ForeignKey(to='registration.RelationshipMaster')),
            ],
        ),
    ]
