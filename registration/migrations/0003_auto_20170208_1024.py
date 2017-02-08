# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20170208_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvprofile',
            name='lastModifiedDateTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pvprofile',
            name='profilePhoto',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pvprofile',
            name='userId',
            field=models.OneToOneField(blank=True, null=True, to='registration.PvUser'),
        ),
    ]
