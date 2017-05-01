# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0032_haha'),
    ]

    operations = [
        migrations.AddField(
            model_name='haha',
            name='tis',
            field=models.CharField(null=True, max_length=30),
        ),
    ]
