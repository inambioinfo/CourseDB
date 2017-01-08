# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-08 15:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('currently_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length_text', models.CharField(max_length=200)),
                ('hours', models.IntegerField(default=0)),
                ('current_cost_pence', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.Duration'),
        ),
    ]
