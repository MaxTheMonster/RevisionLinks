# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-03 10:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('name', models.CharField(max_length=140, unique=True)),
                ('url', models.URLField()),
                ('description', models.CharField(max_length=140)),
                ('date_added', models.DateTimeField(verbose_name='Date Added')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RevisionLinks.Subject'),
        ),
    ]
