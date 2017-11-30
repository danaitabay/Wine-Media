# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 19:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wmedia', '0003_auto_20171111_1342'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['company_name']},
        ),
        migrations.AddField(
            model_name='wineinstance',
            name='MyWine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
