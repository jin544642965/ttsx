# coding:utf-8
from haystack import indexes
from models import GoodsInfo
# 指定对某个模型的数据建立索引


class GoodsInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    # 对哪个模型查询
    def get_model(self):
        return GoodsInfo

    # 对哪些行的数据进行查询
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

