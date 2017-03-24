# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0011_pvsocialhistory_patientid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citymaster',
            name='lastModifiedDateTime',
        ),
        migrations.RemoveField(
            model_name='countrymaster',
            name='lastModifiedDateTime',
        ),
        migrations.RemoveField(
            model_name='familyhistorymaster',
            name='lastModifiedDateTime',
        ),
        migrations.RemoveField(
            model_name='gendermaster',
            name='lastModifiedDateTime',
        ),
        migrations.RemoveField(
            model_name='medicalhistorymaster',
            name='lastModifiedDateTime',
        ),
        migrations.RemoveField(
            model_name='pvfamilyhisotry',
            name='lastModifiedDateTime',
        ),
        migrations.RemoveField(
            model_name='pvfamilyrelationship',
            name='lastModifiedDateTime',
        ),
        migrations.RemoveField(
            model_name='pvmedicalhistory',
            name='lastModifiedDateTime',
        ),
        migrations.RemoveField(
            model_name='pvprofile',
            name='lastModifiedDateTime',
        ),
        migrations.RemoveField(
            model_name='pvsocialhistory',
            name='lastModifiedDateTime',
        ),
        migrations.RemoveField(
            model_name='pvsurgicalhistory',
            name='lastModifiedDateTime',
        ),
        migrations.RemoveField(
            model_name='pvuser',
            name='lastModifiedDateTime',
        ),
        migrations.RemoveField(
            model_name='relationshipmaster',
            name='lastModifiedDateTime',
        ),
        migrations.RemoveField(
            model_name='statemaster',
            name='lastModifiedDateTime',
        ),
        migrations.RemoveField(
            model_name='surgicalhistorymaster',
            name='lastModifiedDateTime',
        ),
    ]
