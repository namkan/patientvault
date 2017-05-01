# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0024_auto_20170306_0721'),
        ('ephr_module', '0002_auto_20170325_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllergyCategoryMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('Substance', models.CharField(max_length=200)),
                ('active_yesNo', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AllergyServerityMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('Substance', models.CharField(max_length=200)),
                ('active_yesNo', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiagnosisStatusMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('status', models.CharField(max_length=100)),
                ('active_yesNo', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DpVisits',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('visit_date', models.DateTimeField()),
                ('visit_time', models.DateTimeField()),
                ('doctor_id', models.ForeignKey(to='ephr_module.DpUser', blank=True, null=True)),
                ('patient_id', models.ForeignKey(to='registration.PvUser', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DrugMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('acive_yesno', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DrugTypeMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('acive_yesno', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='GenericMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('acive_yesno', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Icd10',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('code', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('active_yesNo', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvAllergy',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Substance', models.CharField(max_length=200)),
                ('reactions', models.CharField(max_length=200)),
                ('shared_yesno', models.BooleanField(choices=[('shared', 1), ('no', 0)], default=1)),
                ('acive_yesno', models.BooleanField(default=False)),
                ('created_by_doc', models.BigIntegerField(choices=[('yes', 1), ('no', 0)], blank=True, null=True)),
                ('last_modified_by', models.BigIntegerField(blank=True, null=True)),
                ('last_modified_date_time', models.DateTimeField(auto_now=True, null=True)),
                ('category_id', models.ForeignKey(to='ephr_module.AllergyCategoryMaster', blank=True, null=True)),
                ('created_doc_id', models.ForeignKey(to='ephr_module.DpUser', blank=True, null=True)),
                ('patient_id', models.ForeignKey(to='registration.PvUser', blank=True, null=True)),
                ('serverity_id', models.ForeignKey(to='ephr_module.AllergyServerityMaster', blank=True, null=True)),
                ('visit_id', models.ForeignKey(to='ephr_module.DpVisits', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvLabresults',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('file_path', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PvPrescription',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('rx_no', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100, choices=[('open', 1), ('partially processed', 2), ('processed', 3), ('closed', 4)])),
                ('shared_yesno', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(to='ephr_module.DpUser', blank=True, null=True)),
                ('patient_id', models.ForeignKey(to='registration.PvUser', blank=True, null=True)),
                ('processed_by', models.ForeignKey(to='ephr_module.PhUser', blank=True, null=True)),
                ('visit_id', models.ForeignKey(to='ephr_module.DpVisits', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvPrescriptionDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
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
                ('prescription_id', models.ForeignKey(to='ephr_module.PvPrescription', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvProblemlist',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('freetext_yesno', models.BigIntegerField(choices=[('yes', 1), ('n0', 0)])),
                ('freetext_desc', models.BigIntegerField()),
                ('shared_yesno', models.BooleanField(default=False)),
                ('last_modified_date_time', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(to='ephr_module.DpUser', blank=True, null=True)),
                ('icd_code', models.ForeignKey(to='ephr_module.Icd10', blank=True, null=True)),
                ('patient_id', models.ForeignKey(to='registration.PvUser', blank=True, null=True)),
                ('status', models.ForeignKey(to='ephr_module.DiagnosisStatusMaster', blank=True, null=True)),
                ('visit_id', models.ForeignKey(to='ephr_module.DpVisits', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvRadorders',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('order_status', models.BigIntegerField(choices=[('ordered', 1), ('Inprogress', 2), ('processed', 3)])),
                ('ordered_date', models.DateTimeField(blank=True, null=True)),
                ('processed_on', models.DateTimeField(blank=True, null=True)),
                ('shared_yesno', models.BooleanField(default=True)),
                ('ordered_by', models.ForeignKey(to='ephr_module.DpUser', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvRadresults',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('file_path', models.CharField(max_length=100)),
                ('order_id', models.ForeignKey(to='ephr_module.PvRadorders', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvReminders',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('content', models.CharField(max_length=200)),
                ('status', models.BigIntegerField(choices=[('active', 1), ('closed', 0)])),
                ('reminder_date', models.BigIntegerField()),
                ('created_by', models.ForeignKey(max_length=100, to='ephr_module.DpUser', blank=True, null=True)),
                ('patient_id', models.ForeignKey(to='registration.PvUser', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvUploadedFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('filename', models.CharField(max_length=200)),
                ('file_type', models.CharField(max_length=100)),
                ('file_url', models.URLField(max_length=100, blank=True, null=True)),
                ('added_on', models.DateField(blank=True, null=True)),
                ('is_sharable', models.BooleanField(default=True)),
                ('active_yesno', models.BooleanField(default=True)),
                ('last_modified_date_time', models.DateTimeField(blank=True, null=True)),
                ('last_modified_by', models.ForeignKey(to='registration.PvUser', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RdUser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('acive_yesno', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StrengthMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('acive_yesno', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='VisitStatusMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('acive_yesno', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='pvlaborders',
            name='order_status',
            field=models.CharField(max_length=50, choices=[('ordered', 1), ('Inprogress', 2), ('processed', 3)]),
        ),
        migrations.AddField(
            model_name='pvradorders',
            name='ordered_to',
            field=models.ForeignKey(to='ephr_module.RdUser', blank=True, related_name='tags', null=True),
        ),
        migrations.AddField(
            model_name='pvradorders',
            name='patient_id',
            field=models.ForeignKey(max_length=100, to='registration.PvUser', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pvradorders',
            name='processed_by',
            field=models.ForeignKey(to='ephr_module.RdUser', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pvprescriptiondetails',
            name='strenght_id',
            field=models.ForeignKey(to='ephr_module.StrengthMaster', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dpvisits',
            name='visit_status',
            field=models.ForeignKey(to='ephr_module.VisitStatusMaster', blank=True, null=True),
        ),
    ]
