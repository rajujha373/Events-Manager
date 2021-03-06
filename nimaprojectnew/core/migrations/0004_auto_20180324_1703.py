# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-24 17:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180324_1644'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authuser',
            options={'verbose_name': 'Staff User', 'verbose_name_plural': 'Staff Users'},
        ),
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name': 'Branch', 'verbose_name_plural': 'Branches'},
        ),
        migrations.AddField(
            model_name='user',
            name='branch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Branch'),
            preserve_default=False,
        ),
    ]
