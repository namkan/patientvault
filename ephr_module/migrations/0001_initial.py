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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('active_yesNo', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DpUser',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('active_yesNo', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DpVisits',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('visit_date', models.DateTimeField()),
                ('visit_time', models.DateTimeField()),
                ('doctor_id', models.ForeignKey(to='ephr_module.DpUser', null=True, blank=True)),
                ('patient_id', models.ForeignKey(to='registration.PvUser', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DrugMaster',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('acive_yesno', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DrugTypeMaster',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('acive_yesno', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='GenericMaster',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('acive_yesno', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Icd10',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('acive_yesno', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvAllergy',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Substance', models.CharField(max_length=200)),
                ('reactions', models.CharField(max_length=200)),
                ('shared_yesno', models.BooleanField(choices=[('shared', 1), ('no', 0)], default=1)),
                ('acive_yesno', models.BooleanField(default=False)),
                ('created_by_doc', models.BigIntegerField(choices=[('yes', 1), ('no', 0)], blank=True, null=True)),
                ('last_modified_by', models.BigIntegerField(null=True, blank=True)),
                ('last_modified_date_time', models.DateTimeField(null=True, auto_now=True)),
                ('category_id', models.ForeignKey(to='ephr_module.AllergyCategoryMaster', null=True, blank=True)),
                ('created_doc_id', models.ForeignKey(to='ephr_module.DpUser', null=True, blank=True)),
                ('patient_id', models.ForeignKey(to='registration.PvUser', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvLaborders',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=100, verbose_name=registration.models.PvUser)),
                ('order_status', models.BigIntegerField(choices=[('ordered', 1), ('Inprogress', 2), ('processed', 3)])),
                ('ordered_date', models.DateTimeField(null=True, blank=True)),
                ('processed_on', models.DateTimeField(null=True, blank=True)),
                ('shared_yesno', models.BooleanField(default=True)),
                ('ordered_by', models.ForeignKey(to='ephr_module.DpUser', null=True, blank=True)),
                ('ordered_to', models.ForeignKey(to='ephr_module.PhUser', null=True, blank=True, related_name='tags')),
                ('processed_by', models.ForeignKey(to='ephr_module.PhUser', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvLabresults',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('order_id', models.CharField(max_length=100)),
                ('file_path', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PvPrescription',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('rx_no', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('open', 1), ('partially processed', 2), ('processed', 3), ('closed', 4)], max_length=100)),
                ('shared_yesno', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.ForeignKey(to='ephr_module.DpUser', null=True, blank=True)),
                ('patient_id', models.ForeignKey(to='registration.PvUser', null=True, blank=True)),
                ('processed_by', models.ForeignKey(to='ephr_module.PhUser', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvPrescriptionDetails',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('prescription_type', models.CharField(choices=[('brand based', 1), ('generic', 2), ('free text', 3)], max_length=10)),
                ('free_text', models.TextField(null=True, blank=True)),
                ('dose', models.CharField(max_length=300)),
                ('qnty', models.IntegerField(null=True, blank=True)),
                ('schedule', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(null=True, blank=True)),
                ('end_date', models.DateTimeField(null=True, blank=True)),
                ('instructions', models.TextField(null=True, blank=True)),
                ('created_on', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.ForeignKey(to='ephr_module.DpUser', null=True, blank=True)),
                ('drug_type', models.ForeignKey(to='ephr_module.DrugTypeMaster', null=True, blank=True)),
                ('generic_id', models.ForeignKey(to='ephr_module.GenericMaster', null=True, blank=True)),
                ('prescription_id', models.ForeignKey(to='ephr_module.PvPrescription', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvProblemlist',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('freetext_yesno', models.BigIntegerField(choices=[('yes', 1), ('n0', 0)])),
                ('freetext_desc', models.BigIntegerField()),
                ('shared_yesno', models.BooleanField(default=False)),
                ('last_modified_date_time', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.ForeignKey(to='ephr_module.DpUser', null=True, blank=True)),
                ('patient_id', models.ForeignKey(to='registration.PvUser', null=True, blank=True)),
                ('status', models.ForeignKey(to='ephr_module.DiagnosisStatusMaster', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvRadorders',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('order_status', models.BigIntegerField(choices=[('ordered', 1), ('Inprogress', 2), ('processed', 3)])),
                ('ordered_date', models.DateTimeField(null=True, blank=True)),
                ('processed_on', models.DateTimeField(null=True, blank=True)),
                ('shared_yesno', models.BooleanField(default=True)),
                ('ordered_by', models.ForeignKey(to='ephr_module.DpUser', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvRadresults',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('order_id', models.CharField(max_length=100)),
                ('file_path', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PvReminders',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('status', models.BigIntegerField(choices=[('active', 1), ('closed', 0)])),
                ('reminder_date', models.BigIntegerField()),
                ('created_by', models.ForeignKey(to='registration.PvUser', null=True, blank=True)),
                ('patient_id', models.ForeignKey(max_length=100, null=True, blank=True, to='ephr_module.DpUser')),
            ],
        ),
        migrations.CreateModel(
            name='PvUploadedFiles',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('filename', models.CharField(max_length=200)),
                ('file_type', models.CharField(max_length=100)),
                ('file_url', models.URLField(null=True, max_length=100, blank=True)),
                ('added_on', models.DateField(null=True, blank=True)),
                ('active_yesno', models.BooleanField(default=True)),
                ('last_modified_date_time', models.DateTimeField(null=True, blank=True)),
                ('last_modified_by', models.ForeignKey(to='registration.PvUser', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='RdUser',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('acive_yesno', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StrengthMaster',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('acive_yesno', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='VisitStatusMaster',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('acive_yesno', models.BooleanField(default=False)),
                ('last_modified_by', models.BigIntegerField()),
                ('last_modified_date_time', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='pvradorders',
            name='ordered_to',
            field=models.ForeignKey(to='ephr_module.RdUser', null=True, blank=True, related_name='tags'),
        ),
        migrations.AddField(
            model_name='pvradorders',
            name='patient_id',
            field=models.ForeignKey(max_length=100, null=True, blank=True, to='registration.PvUser'),
        ),
        migrations.AddField(
            model_name='pvradorders',
            name='processed_by',
            field=models.ForeignKey(to='ephr_module.RdUser', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pvprescriptiondetails',
            name='strenght_id',
            field=models.ForeignKey(to='ephr_module.StrengthMaster', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='dpvisits',
            name='visit_status',
            field=models.ForeignKey(to='ephr_module.VisitStatusMaster', null=True, blank=True),
        ),
    ]
