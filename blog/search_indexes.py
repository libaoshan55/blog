#coding=utf8
#该文件的建立是Django框架的规定,然后建立一个XXindex的类
from haystack import indexes
from .models import Post

#为Post创建一个索引（目录）
class PostIndex(indexes.SearchIndex,indexes.Indexable):
    text=indexes.CharField(document=True,use_template=True)

    def get_model(self):
        return Post

    def index_queryset(self,using=None):
        return self.get_model().objects.all()

