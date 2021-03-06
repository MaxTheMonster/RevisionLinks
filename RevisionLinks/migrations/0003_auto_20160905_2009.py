# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-05 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RevisionLinks', '0002_auto_20160903_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='color',
            field=models.ForeignKey(default='Green', on_delete=django.db.models.deletion.CASCADE, to='RevisionLinks.Color'),
            preserve_default=False,
        ),
    ]
