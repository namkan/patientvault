# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0014_auto_20170306_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvfamilyhisotry',
            name='patientId',
            field=models.ForeignKey(blank=True, to='registration.PvUser', null=True),
        ),
        migrations.AddField(
            model_name='pvfamilyrelationship',
            name='patientId',
            field=models.ForeignKey(blank=True, to='registration.PvUser', null=True),
        ),
        migrations.AddField(
            model_name='pvmedicalhistory',
            name='patientId',
            field=models.ForeignKey(blank=True, to='registration.PvUser', null=True),
        ),
        migrations.AddField(
            model_name='pvprofile',
            name='userId',
            field=models.OneToOneField(blank=True, to='registration.PvUser', null=True),
        ),
        migrations.AddField(
            model_name='pvsocialhistory',
            name='patientId',
            field=models.OneToOneField(blank=True, to='registration.PvUser', null=True),
        ),
        migrations.AddField(
            model_name='pvsurgicalhistory',
            name='patientId',
            field=models.ForeignKey(blank=True, to='registration.PvUser', null=True),
        ),
    ]
