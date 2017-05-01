# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0016_auto_20170401_0627'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvlaborders',
            name='order_name',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
    ]
