# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20170208_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvfamilyrelationship',
            name='lastModifiedDateTime',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pvfamilyrelationship',
            name='patientId',
            field=models.ForeignKey(null=True, to='registration.PvUser', blank=True),
        ),
        migrations.AlterField(
            model_name='pvfamilyrelationship',
            name='relationshipId',
            field=models.ForeignKey(null=True, to='registration.RelationshipMaster', blank=True),
        ),
        migrations.AlterField(
            model_name='pvfamilyrelationship',
            name='relativeName',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
    ]
