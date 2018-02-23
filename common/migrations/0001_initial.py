# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-23 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                'db_table': 'goods_banner_image',
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
                'db_table': 'goods_detail_image',
            },
        ),
        migrations.CreateModel(
            name='GoodsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=256)),
                ('market_price', models.IntegerField(db_index=True)),
                ('price', models.IntegerField(db_index=True)),
                ('status', models.IntegerField(db_index=True)),
                ('supply_source', models.CharField(db_index=True, default='', max_length=128)),
                ('supply_item_id', models.CharField(db_index=True, default='', max_length=128)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='GoodsSkuModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('goods_id', models.IntegerField(db_index=True)),
                ('image_url', models.CharField(default='', max_length=1024)),
                ('property_vector', models.CharField(default='', max_length=512)),
                ('price', models.IntegerField(db_index=True, default=0)),
                ('supply_cost', models.IntegerField(db_index=True, default=-1)),
                ('stock', models.IntegerField(db_index=True)),
                ('status', models.IntegerField(db_index=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'goods_sku',
            },
        ),
        migrations.CreateModel(
            name='HomeBannerImageModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.CharField(default='', max_length=1024)),
                ('refer', models.CharField(default='', max_length=1024)),
                ('sort', models.IntegerField(db_index=True)),
                ('status', models.IntegerField(db_index=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'home_banner_image',
            },
        ),
        migrations.CreateModel(
            name='OrderItemModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(db_index=True)),
                ('order_sn', models.CharField(db_index=True, max_length=32)),
                ('goods_id', models.IntegerField()),
                ('goods_name', models.CharField(blank=True, max_length=64)),
                ('sku_id', models.IntegerField()),
                ('sku_property', models.CharField(blank=True, max_length=64)),
                ('sale_price', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'order_item',
            },
        ),
        migrations.CreateModel(
            name='OrderLogisticsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(db_index=True)),
                ('order_sn', models.CharField(db_index=True, max_length=32, unique=True)),
                ('com', models.CharField(max_length=32)),
                ('nu', models.CharField(max_length=32)),
                ('data', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'order_logistics',
            },
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('entry', models.CharField(db_index=True, default='', max_length=32)),
                ('order_sn', models.CharField(default='', max_length=32, unique=True)),
                ('user_id', models.IntegerField(db_index=True)),
                ('total_amount', models.IntegerField(default=0)),
                ('postage', models.IntegerField(default=0)),
                ('amount_payable', models.IntegerField(default=0)),
                ('order_status', models.IntegerField(db_index=True, default=0)),
                ('pintuan_id', models.IntegerField(db_index=True, default=-1)),
                ('pintuan_sn', models.CharField(db_index=True, default='', max_length=32)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderReceiverModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(db_index=True)),
                ('order_sn', models.CharField(max_length=32)),
                ('name', models.CharField(blank=True, max_length=32)),
                ('province', models.CharField(blank=True, max_length=32)),
                ('city', models.CharField(blank=True, max_length=32)),
                ('district', models.CharField(blank=True, max_length=32)),
                ('address', models.CharField(blank=True, max_length=256)),
                ('mobile', models.CharField(blank=True, max_length=16)),
                ('zipcode', models.CharField(blank=True, max_length=10)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'order_receiver',
            },
        ),
        migrations.CreateModel(
            name='OrderTradeModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(db_index=True)),
                ('order_sn', models.CharField(db_index=True, max_length=32)),
                ('trade_no', models.CharField(db_index=True, max_length=32)),
                ('trade_amount', models.IntegerField(default=0)),
                ('trade_status', models.IntegerField(db_index=True, default=0)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'order_trade',
            },
        ),
        migrations.CreateModel(
            name='PintuanModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pintuan_sn', models.CharField(db_index=True, max_length=32, unique=True)),
                ('sku_id', models.IntegerField()),
                ('price', models.IntegerField(db_index=True)),
                ('success_target', models.IntegerField(default=0)),
                ('start_user_id', models.IntegerField(db_index=True)),
                ('pintuan_status', models.IntegerField(db_index=True, default=0)),
                ('finish_time', models.DateTimeField(db_index=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'pintuan',
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=256)),
                ('entry', models.CharField(db_index=True, default='', max_length=64)),
                ('token', models.CharField(db_index=True, default='', max_length=256)),
                ('wx_openid', models.CharField(db_index=True, max_length=256)),
                ('wx_unionid', models.CharField(db_index=True, default='', max_length=256)),
                ('wx_session_key', models.CharField(db_index=True, default='', max_length=256)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
