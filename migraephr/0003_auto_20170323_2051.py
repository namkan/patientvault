# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0002_auto_20170323_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pvuploadedfiles',
            name='last_modified_by',
        ),
        migrations.DeleteModel(
            name='PvUploadedFiles',
        ),
    ]
