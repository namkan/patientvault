# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0012_auto_20170306_0501'),
    ]

    operations = [
        migrations.AddField(
            model_name='citymaster',
            name='lastModifiedDateTime',
            field=models.CharField(null=True, max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='countrymaster',
            name='lastModifiedDateTime',
            field=models.CharField(null=True, max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='familyhistorymaster',
            name='lastModifiedDateTime',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='gendermaster',
            name='lastModifiedDateTime',
            field=models.CharField(null=True, max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='medicalhistorymaster',
            name='lastModifiedDateTime',
            field=models.CharField(null=True, max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='pvfamilyhisotry',
            name='lastModifiedDateTime',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AddField(
            model_name='pvfamilyrelationship',
            name='lastModifiedDateTime',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AddField(
            model_name='pvmedicalhistory',
            name='lastModifiedDateTime',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pvprofile',
            name='lastModifiedDateTime',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AddField(
            model_name='pvsocialhistory',
            name='lastModifiedDateTime',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AddField(
            model_name='pvsurgicalhistory',
            name='lastModifiedDateTime',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AddField(
            model_name='pvuser',
            name='lastModifiedDateTime',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AddField(
            model_name='relationshipmaster',
            name='lastModifiedDateTime',
            field=models.CharField(null=True, max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='statemaster',
            name='lastModifiedDateTime',
            field=models.CharField(null=True, max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='surgicalhistorymaster',
            name='lastModifiedDateTime',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
    ]
