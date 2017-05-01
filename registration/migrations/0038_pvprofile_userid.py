# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0037_remove_pvprofile_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvprofile',
            name='userId',
            field=models.OneToOneField(null=True, blank=True, to='registration.PvUser'),
        ),
    ]
