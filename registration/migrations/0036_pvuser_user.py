# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0035_auto_20170403_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvuser',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, blank=True, null=True),
        ),
    ]
