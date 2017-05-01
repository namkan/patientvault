# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0024_auto_20170306_0721'),
    ]

    operations = [
        migrations.CreateModel(
            name='PvLaborders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('order_status', models.BigIntegerField(choices=[('ordered', 1), ('Inprogress', 2), ('processed', 3)])),
                ('ordered_date', models.DateTimeField(null=True, blank=True)),
                ('processed_on', models.DateTimeField(null=True, blank=True)),
                ('shared_yesno', models.BooleanField(default=True)),
                ('patient_id', models.ForeignKey(to='registration.PvUser', blank=True, null=True)),
            ],
        ),
    ]
