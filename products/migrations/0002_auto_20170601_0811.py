# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 08:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='primart_img',
            new_name='primary_img',
        ),
    ]