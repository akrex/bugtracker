# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='comment',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='issue',
            name='tittle',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='comment',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='topic',
            name='comment',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
