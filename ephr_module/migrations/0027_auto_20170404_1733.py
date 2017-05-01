# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0026_auto_20170403_1125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pvallergy',
            old_name='acive_yesno',
            new_name='active_yesno',
        ),
        migrations.AlterField(
            model_name='pvallergy',
            name='created_by_doc',
            field=models.BooleanField(default=False),
        ),
    ]
