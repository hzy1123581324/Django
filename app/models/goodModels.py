from django.db import models

# Create your models here.
class Banner(models.Model):
    """
    轮播图表
    img:图片链接
    url: 跳转链接
    show: 是否显示
    weight:权重（排列）
    classify: 分类
    """
    # img = models.CharField(max_length=64,unique=True)
    # menus = models.ManyToManyField("Menus",blank=True)
    
class Goods(models.Model):
    '''
    商品表
    '''
    pass

class shop(models.Model):
    '''
    店铺表
    '''
    pass

class Order(models.Model):
    '''
    订单表
    '''
    pass

