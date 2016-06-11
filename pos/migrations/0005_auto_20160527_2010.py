# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0004_order_order_totalprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_totalprice',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=7),
        ),
    ]