# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-08 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('path', models.CharField(max_length=250)),
                ('formata', models.CharField(choices=[('csv', 'CSV'), ('xl', 'Excel'), ('xml', 'XML'), ('json', 'Json')], max_length=10)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='dataset',
            name='tags',
            field=models.ManyToManyField(to='datas.Tag'),
        ),
    ]
