# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0023_auto_20170306_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvfamilyhistory',
            name='relationshipId',
            field=models.ForeignKey(to='registration.RelationshipMaster', null=True, blank=True),
        ),
    ]
