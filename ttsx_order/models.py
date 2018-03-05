# coding:utf-8
from __future__ import unicode_literals

from django.db import models
from ttsx_user.models import UserInfo
from ttsx_goods.models import GoodsInfo
# Create your models here.


class OrderMain(models.Model):
    # 为了数据重复太多，分成2张表
    order_id = models.CharField(max_length=20, primary_key=True)  # 20180129000000uid
    user = models.ForeignKey(UserInfo)
    order_date = models.DateTimeField(auto_now_add=True)  # 添加的时间
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    state = models.IntegerField(default=0)       # 支付状态


class OrderDetail(models.Model):
    order = models.ForeignKey(OrderMain)
    goods = models.ForeignKey(GoodsInfo)
    count = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)   # 促销实际价格又不一样
