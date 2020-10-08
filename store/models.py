from django.db import models

# Create your models here.
# 多商家数据库

class Stores(models.Model):
    """
    店铺（默认是平台）
    店铺id

    店铺地址
    店铺经纬度
    店铺名称
    联系方式（选择）
    店铺所有者
    店铺营业证书
    店铺介绍
    """
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID' )

class Commodity(models.Model):
    '''
    商品表

    商品id
    商品短标题
    商品长标题
    商品价格
    商品限时价格
    商品缩略图
    商品主图
    商品标签    （跟标签表是多对多关系）
    商品优惠券 （跟优惠券表是多对多关系）

    '''

class CommodityDetails(models.Model):
    '''
    商品详情表
    跟商品表是一对一关系
    字段：
    商品轮播图
    商品介绍  （富文本）
    是否收藏
    商品规格
    
    '''