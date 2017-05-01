# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0040_pvuser_aadhar_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pvsocialhistory',
            name='shareYesNo',
        ),
        migrations.AddField(
            model_name='pvsocialhistory',
            name='sharedYesNo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='pvmedicalhistory',
            name='sharedYesNo',
            field=models.BooleanField(default=True),
        ),
    ]
