# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0015_auto_20170325_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pvlaborders',
            old_name='shared_yesno',
            new_name='is_sharable',
        ),
    ]
