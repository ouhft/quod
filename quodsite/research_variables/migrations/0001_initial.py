# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-12 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DictionaryStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DictionaryCategory', models.CharField(max_length=45)),
                ('DictionarySection', models.CharField(max_length=45)),
                ('DictionaryVersion', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserID', models.CharField(max_length=45)),
                ('SessionID', models.PositiveIntegerField()),
                ('SessionVersion', models.CharField(max_length=45)),
                ('SessionTimeStamp', models.CharField(max_length=45)),
                ('SessionVariables', models.TextField(max_length=45)),
                ('SessionName', models.CharField(max_length=45)),
                ('SessionSaves', models.PositiveIntegerField()),
                ('SessionArchived', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VariableVersion', models.CharField(max_length=45)),
                ('VariableCategory', models.CharField(max_length=45)),
                ('VariableSection', models.CharField(max_length=45)),
                ('VariableName', models.CharField(max_length=255)),
                ('VariableDescription', models.TextField()),
            ],
        ),
    ]