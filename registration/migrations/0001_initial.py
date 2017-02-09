# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CityMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CountryMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FamilyhistoryMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='GenderMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=True)),
                ('lastModifiedDateTime', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalhistoryMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PvFamilyHisotry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('sharedYesNo', models.BooleanField(default=True)),
                ('activeYesNo', models.BooleanField()),
                ('lastModifiedDateTime', models.DateTimeField()),
                ('familyhistoryId', models.ForeignKey(to='registration.FamilyhistoryMaster')),
            ],
        ),
        migrations.CreateModel(
            name='PvFamilyRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('relativeName', models.CharField(blank=True, null=True, max_length=30)),
                ('lastModifiedDateTime', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvMedicalHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('sharedYesNo', models.BooleanField(default=False)),
                ('activeYesNo', models.BooleanField(default=True)),
                ('lastModifiedDateTime', models.DateTimeField()),
                ('mediacalHistoryId', models.ForeignKey(to='registration.MedicalhistoryMaster', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('profilePhoto', models.TextField(blank=True, null=True)),
                ('address', models.CharField(blank=True, null=True, max_length=100)),
                ('lastModifiedDateTime', models.DateTimeField(blank=True, null=True)),
                ('cityId', models.ForeignKey(to='registration.CityMaster', blank=True, null=True)),
                ('countryId', models.ForeignKey(to='registration.CountryMaster', blank=True, null=True)),
                ('gender', models.ForeignKey(to='registration.GenderMaster', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvSocialHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('alcoholUsage', models.IntegerField(blank=True, null=True)),
                ('drinksPerWeek', models.IntegerField(blank=True, null=True)),
                ('tobacoUsage', models.IntegerField(blank=True, null=True)),
                ('tobacoQuitDate', models.DateField(blank=True, null=True)),
                ('drugUsage', models.IntegerField(blank=True, null=True)),
                ('drugDetails', models.CharField(max_length=250)),
                ('shareYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PvSurgicalHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('sharedYesNo', models.BooleanField(default=True)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PvUser',
            fields=[
                ('userId', models.AutoField(serialize=False, primary_key=True)),
                ('mobile_number', models.BigIntegerField(unique=True)),
                ('email', models.CharField(max_length=50)),
                ('activationToken', models.CharField(blank=True, null=True, max_length=20)),
                ('activationAttempts', models.IntegerField(default=0, blank=True, null=True)),
                ('isProfileComplete', models.BooleanField(default=False)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.DateTimeField(auto_now_add=True)),
                ('otpTime', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RelationshipMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=True)),
                ('lastModifiedDateTime', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StateMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.CharField(max_length=30)),
                ('country', models.ForeignKey(to='registration.CountryMaster')),
            ],
        ),
        migrations.CreateModel(
            name='SurgicalhistoryMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='pvsurgicalhistory',
            name='patientId',
            field=models.OneToOneField(to='registration.PvUser', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pvsurgicalhistory',
            name='surgicalhistoryId',
            field=models.ForeignKey(to='registration.SurgicalhistoryMaster', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pvsocialhistory',
            name='patientId',
            field=models.OneToOneField(to='registration.PvUser'),
        ),
        migrations.AddField(
            model_name='pvprofile',
            name='stateId',
            field=models.ForeignKey(to='registration.StateMaster', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pvprofile',
            name='userId',
            field=models.OneToOneField(to='registration.PvUser', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pvmedicalhistory',
            name='patientId',
            field=models.ForeignKey(to='registration.PvUser', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pvfamilyrelationship',
            name='patientId',
            field=models.ForeignKey(to='registration.PvUser', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pvfamilyrelationship',
            name='relationshipId',
            field=models.ForeignKey(to='registration.RelationshipMaster', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pvfamilyrelationship',
            name='relative',
            field=models.ForeignKey(related_name='relative', to='registration.PvUser', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pvfamilyhisotry',
            name='patientId',
            field=models.OneToOneField(to='registration.PvUser'),
        ),
        migrations.AddField(
            model_name='pvfamilyhisotry',
            name='relationshipId',
            field=models.ForeignKey(to='registration.RelationshipMaster'),
        ),
        migrations.AddField(
            model_name='citymaster',
            name='state',
            field=models.ForeignKey(to='registration.StateMaster'),
        ),
    ]
