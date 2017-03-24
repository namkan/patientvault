# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20170306_0353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pvsocialhistory',
            name='drugDetails',
        ),
    ]
