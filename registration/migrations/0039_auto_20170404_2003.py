# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0038_pvprofile_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvmedicalhistory',
            name='current_status',
            field=models.CharField(blank=True, null=True, choices=[('Active', 1), ('Resolved', 2)], max_length=100),
        ),
        migrations.AddField(
            model_name='pvmedicalhistory',
            name='resolved_on',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pvmedicalhistory',
            name='started_on',
            field=models.DateField(blank=True, null=True),
        ),
    ]
