# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0034_remove_haha_tis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pvuser',
            name='user',
        ),
        migrations.AlterField(
            model_name='pvuser',
            name='id',
            field=models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False),
        ),
    ]
