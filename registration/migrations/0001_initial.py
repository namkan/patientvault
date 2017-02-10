# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CityMaster',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CountryMaster',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FamilyhistoryMaster',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='GenderMaster',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=True)),
                ('lastModifiedDateTime', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalhistoryMaster',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PvFamilyHisotry',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('sharedYesNo', models.BooleanField(default=True)),
                ('activeYesNo', models.BooleanField()),
                ('lastModifiedDateTime', models.DateTimeField()),
                ('familyhistoryId', models.ForeignKey(to='registration.FamilyhistoryMaster')),
            ],
        ),
        migrations.CreateModel(
            name='PvFamilyRelationship',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('relativeName', models.CharField(max_length=30, null=True, blank=True)),
                ('lastModifiedDateTime', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PvMedicalHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('sharedYesNo', models.BooleanField(default=False)),
                ('activeYesNo', models.BooleanField(default=True)),
                ('lastModifiedDateTime', models.DateTimeField()),
                ('mediacalHistoryId', models.ForeignKey(null=True, blank=True, to='registration.MedicalhistoryMaster')),
            ],
        ),
        migrations.CreateModel(
            name='PvProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('dob', models.DateField(null=True, blank=True)),
                ('profilePhoto', models.TextField(null=True, blank=True)),
                ('address', models.CharField(max_length=100, null=True, blank=True)),
                ('lastModifiedDateTime', models.DateTimeField(null=True, blank=True)),
                ('cityId', models.ForeignKey(null=True, blank=True, to='registration.CityMaster')),
                ('countryId', models.ForeignKey(null=True, blank=True, to='registration.CountryMaster')),
                ('gender', models.ForeignKey(null=True, blank=True, to='registration.GenderMaster')),
            ],
        ),
        migrations.CreateModel(
            name='PvSocialHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('sharedYesNo', models.BooleanField(default=True)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PvUser',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('mobile_number', models.BigIntegerField(unique=True)),
                ('email', models.CharField(max_length=50)),
                ('activationToken', models.CharField(max_length=20, null=True, blank=True)),
                ('activationAttempts', models.IntegerField(null=True, default=0, blank=True)),
                ('isProfileComplete', models.BooleanField(default=False)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.DateTimeField(auto_now_add=True)),
                ('pTime', models.DateTimeField(null=True, blank=True)),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RelationshipMaster',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=True)),
                ('lastModifiedDateTime', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StateMaster',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('activeYesNo', models.BooleanField(default=False)),
                ('lastModifiedDateTime', models.CharField(max_length=30)),
                ('country', models.ForeignKey(to='registration.CountryMaster')),
            ],
        ),
        migrations.CreateModel(
            name='SurgicalhistoryMaster',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
            field=models.ForeignKey(null=True, blank=True, to='registration.SurgicalhistoryMaster'),
        ),
        migrations.AddField(
            model_name='pvsocialhistory',
            name='patientId',
            field=models.OneToOneField(to='registration.PvUser'),
        ),
        migrations.AddField(
            model_name='pvprofile',
            name='stateId',
            field=models.ForeignKey(null=True, blank=True, to='registration.StateMaster'),
        ),
        migrations.AddField(
            model_name='pvprofile',
            name='userId',
            field=models.OneToOneField(null=True, blank=True, to='registration.PvUser'),
        ),
        migrations.AddField(
            model_name='pvmedicalhistory',
            name='patientId',
            field=models.ForeignKey(null=True, blank=True, to='registration.PvUser'),
        ),
        migrations.AddField(
            model_name='pvfamilyrelationship',
            name='patientId',
            field=models.ForeignKey(null=True, blank=True, to='registration.PvUser'),
        ),
        migrations.AddField(
            model_name='pvfamilyrelationship',
            name='relationshipId',
            field=models.ForeignKey(null=True, blank=True, to='registration.RelationshipMaster'),
        ),
        migrations.AddField(
            model_name='pvfamilyrelationship',
            name='relative',
            field=models.ForeignKey(null=True, blank=True, related_name='relative', to='registration.PvUser'),
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
