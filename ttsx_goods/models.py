# coding:utf-8
from __future__ import unicode_literals

from django.db import models

from tinymce.models import HTMLField
# Create your models here.
# 根据首页有商品分类信息

# 商品信息

# 商品与分类的关系，一个商品属于某一个分类


class TypeInfo(models.Model):
    title = models.CharField(max_length=50)
    isDelete = models.BooleanField(False)

    def __str__(self):
        return self.title.encode('utf-8')


class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=50)
    gprice = models.DecimalField(max_digits=5, decimal_places=2)  # 999.99
    gunit = models.CharField(max_length=20)
    gkucun = models.IntegerField(default=100)
    # 富文本编辑器
    gcontent = HTMLField()
    gpic = models.ImageField(upload_to='goods')
    isDelete = models.BooleanField(default=False)
    gclick = models.IntegerField(default=0)
    gtype = models.ForeignKey('TypeInfo')
    gsubtitle = models.CharField(max_length=200)

    def __str__(self):
        return self.gtitle.encode('utf-8')