# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20170306_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='surgicalhistorymaster',
            name='lastModifiedDateTime',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='surgicalhistorymaster',
            name='name',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='familyhistorymaster',
            name='lastModifiedDateTime',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
    ]
