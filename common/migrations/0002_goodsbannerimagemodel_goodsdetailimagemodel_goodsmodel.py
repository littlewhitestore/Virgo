# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-24 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsBannerImageModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('goods_id', models.IntegerField(db_index=True)),
                ('url', models.CharField(default='', max_length=1024)),
                ('sort', models.IntegerField(db_index=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'common_goods_banner_image',
            },
        ),
        migrations.CreateModel(
            name='GoodsDetailImageModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('goods_id', models.IntegerField(db_index=True)),
                ('url', models.CharField(default='', max_length=1024)),
                ('sort', models.IntegerField(db_index=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'common_goods_detail_image',
            },
        ),
        migrations.CreateModel(
            name='GoodsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=256)),
                ('taobao_id', models.CharField(db_index=True, default='', max_length=128)),
                ('market_price', models.IntegerField(db_index=True)),
                ('price', models.IntegerField(db_index=True)),
                ('status', models.IntegerField(db_index=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'common_goods',
            },
        ),
    ]