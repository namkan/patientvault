# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0039_auto_20170404_2003'),
        ('ephr_module', '0033_auto_20170404_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='PvPrescriptionDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('prescription_type', models.CharField(choices=[('brand based', 1), ('generic', 2), ('free text', 3)], max_length=10)),
                ('free_text', models.TextField(blank=True, null=True)),
                ('dose', models.CharField(max_length=300)),
                ('qnty', models.IntegerField(blank=True, null=True)),
                ('schedule', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('instructions', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, to='ephr_module.DpUser')),
                ('drug_id', models.ForeignKey(blank=True, null=True, to='ephr_module.DrugMaster')),
                ('drug_type', models.ForeignKey(blank=True, null=True, to='ephr_module.DrugTypeMaster')),
                ('generic_id', models.ForeignKey(blank=True, null=True, to='ephr_module.GenericMaster')),
                ('patient_id', models.ForeignKey(blank=True, null=True, to='registration.PvUser')),
                ('prescription_id', models.ForeignKey(blank=True, null=True, to='ephr_module.PvPrescription')),
                ('strenght_id', models.ForeignKey(blank=True, null=True, to='ephr_module.StrengthMaster')),
            ],
        ),
    ]
