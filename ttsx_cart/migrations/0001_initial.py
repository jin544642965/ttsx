# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-01-26 17:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ttsx_goods', '0002_auto_20180106_2147'),
        ('ttsx_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ttsx_goods.GoodsInfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ttsx_user.UserInfo')),
            ],
        ),
    ]
