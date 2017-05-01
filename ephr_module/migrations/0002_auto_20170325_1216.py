# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DpUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('active_yesNo', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('acive_yesno', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='pvlaborders',
            name='ordered_by',
            field=models.ForeignKey(blank=True, null=True, to='ephr_module.DpUser'),
        ),
        migrations.AddField(
            model_name='pvlaborders',
            name='ordered_to',
            field=models.ForeignKey(blank=True, null=True, to='ephr_module.PhUser', related_name='tags'),
        ),
        migrations.AddField(
            model_name='pvlaborders',
            name='processed_by',
            field=models.ForeignKey(blank=True, null=True, to='ephr_module.PhUser'),
        ),
    ]
