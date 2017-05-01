# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0019_auto_20170402_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvlaborders',
            name='checkbox_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='pvradorders',
            name='checkbox_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='pvuploadedfiles',
            name='checkbox_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
