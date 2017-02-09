# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_remove_pvuser_otptime'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvuser',
            name='otpTime',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]