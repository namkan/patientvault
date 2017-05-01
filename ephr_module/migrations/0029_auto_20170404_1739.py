# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0028_auto_20170404_1735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pvallergy',
            old_name='acive_yesno',
            new_name='active_yesno',
        ),
    ]
