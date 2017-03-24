# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ephr_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvallergy',
            name='serverity_id',
            field=models.ForeignKey(blank=True, to='ephr_module.AllergyServerityMaster', null=True),
        ),
        migrations.AddField(
            model_name='pvallergy',
            name='visit_id',
            field=models.ForeignKey(blank=True, to='ephr_module.DpVisits', null=True),
        ),
        migrations.AddField(
            model_name='pvprescription',
            name='visit_id',
            field=models.ForeignKey(blank=True, to='ephr_module.DpVisits', null=True),
        ),
        migrations.AddField(
            model_name='pvprescriptiondetails',
            name='drug_id',
            field=models.ForeignKey(blank=True, to='ephr_module.DrugMaster', null=True),
        ),
        migrations.AddField(
            model_name='pvproblemlist',
            name='icd_code',
            field=models.ForeignKey(blank=True, to='ephr_module.Icd10', null=True),
        ),
        migrations.AddField(
            model_name='pvproblemlist',
            name='visit_id',
            field=models.ForeignKey(blank=True, to='ephr_module.DpVisits', null=True),
        ),
    ]
