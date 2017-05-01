# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0023_auto_20170402_1456'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pvprescription',
            old_name='shared_yesno',
            new_name='is_sharable',
        ),
    ]
