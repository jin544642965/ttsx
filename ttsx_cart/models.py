# coding:utf-8
from __future__ import unicode_literals

from django.db import models
from ttsx_goods.models import GoodsInfo
# Create your models here.


class CartInfo(models.Model):
    # 谁买了多少个什么
    user = models.ForeignKey('ttsx_user.UserInfo')  # 两种方式均可
    goods = models.ForeignKey(GoodsInfo)  # 商品是唯一属性，对多个用户，作为外键
    count = models.IntegerField()

