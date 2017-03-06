# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20170228_0622'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvfamilyhisotry',
            name='familyhistoryStatus',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='familyhistorymaster',
            name='lastModifiedDateTime',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='familyhistorymaster',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pvfamilyhisotry',
            name='patientId',
            field=models.ForeignKey(to='registration.PvUser'),
        ),
        migrations.AlterField(
            model_name='pvsurgicalhistory',
            name='patientId',
            field=models.ForeignKey(null=True, blank=True, to='registration.PvUser'),
        ),
    ]
