# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-11 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wmedia', '0002_auto_20171108_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='Established_date',
            new_name='established_date',
        ),
        migrations.AddField(
            model_name='wineinstance',
            name='wine_type',
            field=models.CharField(max_length=20, null=True, verbose_name=b'Catagory'),
        ),
    ]
