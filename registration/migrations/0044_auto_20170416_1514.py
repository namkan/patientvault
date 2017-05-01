# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0043_auto_20170416_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvuser',
            name='shareFamily',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pvuser',
            name='shareMedical',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pvuser',
            name='shareSocial',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pvuser',
            name='shareSurgical',
            field=models.BooleanField(default=True),
        ),
    ]
