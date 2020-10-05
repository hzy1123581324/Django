from django.db import models

# Create your models here.
# 多商家数据库

class Stores(models.Model):
    """
    店铺（默认是平台）
    地址
    经纬度
    店铺名称
    联系方式（选择）
    
    """
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID' )