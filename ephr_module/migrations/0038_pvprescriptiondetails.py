# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0039_auto_20170404_2003'),
        ('ephr_module', '0037_auto_20170404_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='PvPrescriptionDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('prescription_type', models.CharField(max_length=10, choices=[('brand based', 1), ('generic', 2), ('free text', 3)])),
                ('free_text', models.TextField(blank=True, null=True)),
                ('dose', models.CharField(max_length=300)),
                ('qnty', models.IntegerField(blank=True, null=True)),
                ('schedule', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('instructions', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(to='ephr_module.DpUser', blank=True, null=True)),
                ('drug_id', models.ForeignKey(to='ephr_module.DrugMaster', blank=True, null=True)),
                ('drug_type', models.ForeignKey(to='ephr_module.DrugTypeMaster', blank=True, null=True)),
                ('generic_id', models.ForeignKey(to='ephr_module.GenericMaster', blank=True, null=True)),
                ('patient_id', models.ForeignKey(to='registration.PvUser', blank=True, null=True)),
                ('prescription_id', models.ForeignKey(to='ephr_module.PvPrescription', blank=True, null=True)),
                ('strenght_id', models.ForeignKey(to='ephr_module.StrengthMaster', blank=True, null=True)),
            ],
        ),
    ]
