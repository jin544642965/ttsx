# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-01-05 19:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gtitle', models.CharField(max_length=50)),
                ('gprice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('gunit', models.CharField(max_length=20)),
                ('gkuncun', models.IntegerField(default=100)),
                ('gcontent', tinymce.models.HTMLField()),
                ('gpic', models.ImageField(upload_to='goods')),
                ('isDelete', models.BooleanField(default=False)),
                ('gclick', models.IntegerField(default=0)),
                ('gsubtitle', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('isDelete', models.BooleanField(verbose_name=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ttsx_goods.TypeInfo'),
        ),
    ]
