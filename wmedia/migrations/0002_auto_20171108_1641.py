# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-08 21:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wmedia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(help_text=b'Enter type of wine (e.g. Red wine, White wine, Rose)', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=20)),
                ('Established_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand_name', models.CharField(max_length=20)),
                ('Description', models.TextField(help_text=b'Enter a brief description of the wine', max_length=1000)),
                ('bottled_date', models.DateTimeField(blank=True, null=True)),
                ('company_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wmedia.Company')),
                ('types', models.ManyToManyField(help_text=b'Select a type of wine', to='wmedia.Catagory')),
            ],
        ),
        migrations.CreateModel(
            name='WineInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text=b'Unique ID for this particular wine', primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, choices=[(b'o', b'Out of stock'), (b'a', b'Available')], default=b'a', help_text=b'Wine availability', max_length=1)),
                ('wine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wmedia.Wine')),
            ],
            options={
                'ordering': ['wine'],
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
