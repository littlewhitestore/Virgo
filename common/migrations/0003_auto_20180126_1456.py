# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-26 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_goodsbannerimagemodel_goodsdetailimagemodel_goodsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderTrade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_sn', models.CharField(max_length=32)),
                ('trade_no', models.CharField(max_length=32)),
                ('trade_amount', models.IntegerField(default=0)),
                ('trade_status', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'oms_order_trade',
            },
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderreceiver',
            name='order',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order_sn',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderreceiver',
            name='order_sn',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderreceiver',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
