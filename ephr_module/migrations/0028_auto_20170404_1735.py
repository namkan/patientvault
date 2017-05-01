# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0027_auto_20170404_1733'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pvallergy',
            old_name='active_yesno',
            new_name='acive_yesno',
        ),
        migrations.RemoveField(
            model_name='pvallergy',
            name='created_by_doc',
        ),
    ]
