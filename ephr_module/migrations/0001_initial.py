# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import registration.models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0024_auto_20170306_0721'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllergyCategoryMaster',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('Substance', models.CharField(max_length=200)),
                ('active_yesNo', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AllergyServerityMaster',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('Substance', models.CharField(max_length=200)),
                ('active_yesNo', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiagnosisStatusMaster',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('status', models.CharField(max_length=100)),
                ('active_yesNo', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DpUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('active_yesNo', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DpVisits',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('visit_date', models.DateTimeField()),
                ('visit_time', models.DateTimeField()),
                ('doctor_id', models.ForeignKey(null=True, to='ephr_module.DpUser', blank=True)),
                ('patient_id', models.ForeignKey(null=True, to='registration.PvUser', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DrugMaster',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('acive_yesno', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DrugTypeMaster',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('acive_yesno', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='GenericMaster',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('acive_yesno', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Icd10',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('code', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('active_yesNo', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('acive_yesno', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvAllergy',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('Substance', models.CharField(max_length=200)),
                ('reactions', models.CharField(max_length=200)),
                ('shared_yesno', models.BooleanField(default=1, choices=[('shared', 1), ('no', 0)])),
                ('acive_yesno', models.BooleanField(default=False)),
                ('created_by_doc', models.BigIntegerField(null=True, blank=True, choices=[('yes', 1), ('no', 0)])),
                ('last_modified_by', models.BigIntegerField(null=True, blank=True)),
                ('last_modified_date_time', models.DateTimeField(null=True, auto_now=True)),
                ('category_id', models.ForeignKey(null=True, to='ephr_module.AllergyCategoryMaster', blank=True)),
                ('created_doc_id', models.ForeignKey(null=True, to='ephr_module.DpUser', blank=True)),
                ('patient_id', models.ForeignKey(null=True, to='registration.PvUser', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvLaborders',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('patient_id', models.CharField(max_length=100, verbose_name=registration.models.PvUser)),
                ('order_status', models.BigIntegerField(choices=[('ordered', 1), ('Inprogress', 2), ('processed', 3)])),
                ('ordered_date', models.DateTimeField(null=True, blank=True)),
                ('processed_on', models.DateTimeField(null=True, blank=True)),
                ('shared_yesno', models.BooleanField(default=True)),
                ('ordered_by', models.ForeignKey(null=True, to='ephr_module.DpUser', blank=True)),
                ('ordered_to', models.ForeignKey(null=True, related_name='tags', to='ephr_module.PhUser', blank=True)),
                ('processed_by', models.ForeignKey(null=True, to='ephr_module.PhUser', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvLabresults',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('order_id', models.CharField(max_length=100)),
                ('file_path', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PvPrescription',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('rx_no', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100, choices=[('open', 1), ('partially processed', 2), ('processed', 3), ('closed', 4)])),
                ('shared_yesno', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.ForeignKey(null=True, to='ephr_module.DpUser', blank=True)),
                ('patient_id', models.ForeignKey(null=True, to='registration.PvUser', blank=True)),
                ('processed_by', models.ForeignKey(null=True, to='ephr_module.PhUser', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvPrescriptionDetails',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('prescription_type', models.CharField(max_length=10, choices=[('brand based', 1), ('generic', 2), ('free text', 3)])),
                ('free_text', models.TextField(null=True, blank=True)),
                ('dose', models.CharField(max_length=300)),
                ('qnty', models.IntegerField(null=True, blank=True)),
                ('schedule', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(null=True, blank=True)),
                ('end_date', models.DateTimeField(null=True, blank=True)),
                ('instructions', models.TextField(null=True, blank=True)),
                ('created_on', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.ForeignKey(null=True, to='ephr_module.DpUser', blank=True)),
                ('drug_type', models.ForeignKey(null=True, to='ephr_module.DrugTypeMaster', blank=True)),
                ('generic_id', models.ForeignKey(null=True, to='ephr_module.GenericMaster', blank=True)),
                ('prescription_id', models.ForeignKey(null=True, to='ephr_module.PvPrescription', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvProblemlist',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('freetext_yesno', models.BigIntegerField(choices=[('yes', 1), ('n0', 0)])),
                ('freetext_desc', models.BigIntegerField()),
                ('shared_yesno', models.BooleanField(default=False)),
                ('last_modified_date_time', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.ForeignKey(null=True, to='ephr_module.DpUser', blank=True)),
                ('patient_id', models.ForeignKey(null=True, to='registration.PvUser', blank=True)),
                ('status', models.ForeignKey(null=True, to='ephr_module.DiagnosisStatusMaster', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvRadorders',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('order_status', models.BigIntegerField(choices=[('ordered', 1), ('Inprogress', 2), ('processed', 3)])),
                ('ordered_date', models.DateTimeField(null=True, blank=True)),
                ('processed_on', models.DateTimeField(null=True, blank=True)),
                ('shared_yesno', models.BooleanField(default=True)),
                ('ordered_by', models.ForeignKey(null=True, to='ephr_module.DpUser', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvRadresults',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('order_id', models.CharField(max_length=100)),
                ('file_path', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PvReminders',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('content', models.CharField(max_length=200)),
                ('status', models.BigIntegerField(choices=[('active', 1), ('closed', 0)])),
                ('reminder_date', models.BigIntegerField()),
                ('created_by', models.ForeignKey(null=True, to='registration.PvUser', blank=True)),
                ('patient_id', models.ForeignKey(null=True, to='ephr_module.DpUser', max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvUploadedFiles',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('filename', models.CharField(max_length=200)),
                ('file_type', models.CharField(max_length=100)),
                ('file_url', models.URLField(null=True, max_length=100, blank=True)),
                ('added_on', models.DateField(null=True, blank=True)),
                ('active_yesno', models.BooleanField(default=True)),
                ('last_modified_date_time', models.DateTimeField(null=True, blank=True)),
                ('last_modified_by', models.ForeignKey(null=True, to='registration.PvUser', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='RdUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('acive_yesno', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StrengthMaster',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('acive_yesno', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='VisitStatusMaster',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('acive_yesno', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='pvradorders',
            name='ordered_to',
            field=models.ForeignKey(null=True, related_name='tags', to='ephr_module.RdUser', blank=True),
        ),
        migrations.AddField(
            model_name='pvradorders',
            name='patient_id',
            field=models.ForeignKey(null=True, to='registration.PvUser', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='pvradorders',
            name='processed_by',
            field=models.ForeignKey(null=True, to='ephr_module.RdUser', blank=True),
        ),
        migrations.AddField(
            model_name='pvprescriptiondetails',
            name='strenght_id',
            field=models.ForeignKey(null=True, to='ephr_module.StrengthMaster', blank=True),
        ),
        migrations.AddField(
            model_name='dpvisits',
            name='visit_status',
            field=models.ForeignKey(null=True, to='ephr_module.VisitStatusMaster', blank=True),
        ),
    ]
