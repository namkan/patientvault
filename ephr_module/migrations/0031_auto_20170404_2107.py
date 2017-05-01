# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0030_pvallergy_created_by_doc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pvallergy',
            old_name='Substance',
            new_name='substance',
        ),
    ]
