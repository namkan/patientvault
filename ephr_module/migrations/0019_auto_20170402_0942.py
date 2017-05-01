# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0018_pvradorders_order_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pvradorders',
            old_name='shared_yesno',
            new_name='is_sharable',
        ),
    ]
