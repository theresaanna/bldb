# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_number', models.IntegerField()),
                ('date_added', models.DateField()),
                ('added_by', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=1)),
                ('lesion_location', models.CharField(max_length=50)),
                ('lesion_etiology', models.CharField(max_length=50)),
                ('incident_date', models.DateField()),
                ('incident_date_is_exact', models.CharField(max_length=3)),
                ('type_of_np_data', models.CharField(max_length=50)),
                ('patient_notes', models.CharField(max_length=250)),
                ('studies_using_data', models.CharField(max_length=250)),
                ('people_currently_analyzing', models.CharField(max_length=50)),
            ],
        ),
    ]
