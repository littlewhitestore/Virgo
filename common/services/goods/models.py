# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class GoodsModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, default='')
    market_price = models.IntegerField(null=False, db_index=True)
    price = models.IntegerField(null=False, db_index=True)
    status = models.IntegerField(null=False, db_index=True)
    supply_source = models.CharField(max_length=128, default='', db_index=True)
    supply_item_id = models.CharField(max_length=128, default='', db_index=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'goods'

class GoodsSkuModel(models.Model):
    id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField(null=False, db_index=True)
    image_key = models.CharField(max_length=64, default='')
    property_vector = models.CharField(max_length=512, default='')
    price = models.IntegerField(null=False, db_index=True)
    pintuan_price = models.IntegerField(null=False, db_index=True)
    supply_cost= models.IntegerField(null=False, db_index=True)
    stock = models.IntegerField(null=False, db_index=True)
    status = models.IntegerField(null=False, db_index=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'goods_sku'

class GoodsBannerImageModel(models.Model):
    id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField(null=False, db_index=True)
    image_key = models.CharField(max_length=64, default='')
    sort = models.IntegerField(null=False, db_index=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'goods_banner_image'


class GoodsDetailImageModel(models.Model):
    id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField(null=False, db_index=True)
    image_key = models.CharField(max_length=64, default='')
    sort = models.IntegerField(null=False, db_index=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'goods_detail_image'
