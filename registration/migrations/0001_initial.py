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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CountryMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FamilyhistoryMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='GenderMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=True)),
                ('lastModifiedDateTime', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalhistoryMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PvFamilyHisotry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sharedYesNo', models.BooleanField(default=True)),
                ('activeYesNo', models.BooleanField()),
                ('lastModifiedDateTime', models.DateTimeField()),
                ('familyhistoryId', models.ForeignKey(to='registration.FamilyhistoryMaster')),
            ],
        ),
        migrations.CreateModel(
            name='PvFamilyRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relativeName', models.CharField(max_length=30, null=True, blank=True)),
                ('lastModifiedDateTime', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvMedicalHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sharedYesNo', models.BooleanField(default=False)),
                ('activeYesNo', models.BooleanField(default=True)),
                ('lastModifiedDateTime', models.DateTimeField()),
                ('mediacalHistoryId', models.ForeignKey(blank=True, to='registration.MedicalhistoryMaster', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dob', models.DateField(null=True, blank=True)),
                ('profilePhoto', models.TextField(null=True, blank=True)),
                ('address', models.CharField(max_length=100, null=True, blank=True)),
                ('lastModifiedDateTime', models.DateTimeField(null=True, blank=True)),
                ('cityId', models.ForeignKey(blank=True, to='registration.CityMaster', null=True)),
                ('countryId', models.ForeignKey(blank=True, to='registration.CountryMaster', null=True)),
                ('gender', models.ForeignKey(blank=True, to='registration.GenderMaster', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvSocialHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alcoholUsage', models.IntegerField(null=True, blank=True)),
                ('drinksPerWeek', models.IntegerField(null=True, blank=True)),
                ('tobacoUsage', models.IntegerField(null=True, blank=True)),
                ('tobacoQuitDate', models.DateField(null=True, blank=True)),
                ('drugUsage', models.IntegerField(null=True, blank=True)),
                ('drugDetails', models.CharField(max_length=250)),
                ('shareYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PvSurgicalHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('activationToken', models.CharField(max_length=20, null=True, blank=True)),
                ('activationAttempts', models.IntegerField(default=0, null=True, blank=True)),
                ('isProfileComplete', models.BooleanField(default=False)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('otpTime', models.DateTimeField(null=True, blank=True)),
                ('lastModifiedDateTime', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RelationshipMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=True)),
                ('lastModifiedDateTime', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StateMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.CharField(max_length=30)),
                ('country', models.ForeignKey(to='registration.CountryMaster')),
            ],
        ),
        migrations.CreateModel(
            name='SurgicalhistoryMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='pvsurgicalhistory',
            name='patientId',
            field=models.OneToOneField(null=True, blank=True, to='registration.PvUser'),
        ),
        migrations.AddField(
            model_name='pvsurgicalhistory',
            name='surgicalhistoryId',
            field=models.ForeignKey(blank=True, to='registration.SurgicalhistoryMaster', null=True),
        ),
        migrations.AddField(
            model_name='pvsocialhistory',
            name='patientId',
            field=models.OneToOneField(to='registration.PvUser'),
        ),
        migrations.AddField(
            model_name='pvprofile',
            name='stateId',
            field=models.ForeignKey(blank=True, to='registration.StateMaster', null=True),
        ),
        migrations.AddField(
            model_name='pvprofile',
            name='userId',
            field=models.OneToOneField(null=True, blank=True, to='registration.PvUser'),
        ),
        migrations.AddField(
            model_name='pvmedicalhistory',
            name='patientId',
            field=models.ForeignKey(blank=True, to='registration.PvUser', null=True),
        ),
        migrations.AddField(
            model_name='pvfamilyrelationship',
            name='patientId',
            field=models.ForeignKey(blank=True, to='registration.PvUser', null=True),
        ),
        migrations.AddField(
            model_name='pvfamilyrelationship',
            name='relationshipId',
            field=models.ForeignKey(blank=True, to='registration.RelationshipMaster', null=True),
        ),
        migrations.AddField(
            model_name='pvfamilyrelationship',
            name='relative',
            field=models.ForeignKey(related_name='relative', blank=True, to='registration.PvUser', null=True),
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
