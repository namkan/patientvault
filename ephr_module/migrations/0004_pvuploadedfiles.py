# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0024_auto_20170306_0721'),
        ('ephr_module', '0003_auto_20170323_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='PvUploadedFiles',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('filename', models.CharField(max_length=200)),
                ('file_type', models.CharField(max_length=100)),
                ('file_url', models.URLField(max_length=100, blank=True, null=True)),
                ('added_on', models.DateField(blank=True, null=True)),
                ('active_yesno', models.BooleanField(default=True)),
                ('last_modified_date_time', models.DateTimeField(blank=True, null=True)),
                ('last_modified_by', models.ForeignKey(to='registration.PvUser', null=True, blank=True)),
            ],
        ),
    ]
