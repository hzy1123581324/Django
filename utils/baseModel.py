
from django.db import models
import datetime


class BaseModel(models.Model):
    """为模型类补充字段"""

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    id = models.AutoField(auto_created=True, primary_key=True,
                          serialize=False, verbose_name='ID')

    class Meta:
        # abstract: 抽象
        abstract = True  # 说明是抽象模型类, 用于继承使用，数据库迁移时不会创建BaseModel的表


class CategoryModel(models.Model):
    '''
    分类继承
    '''
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )
    name = models.CharField(default="", max_length=30,
                            verbose_name="类别名",  help_text="类别名")
    code = models.CharField(default="",  max_length=30,
                            verbose_name="类别code", help_text="类别code")
    desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
    category_type = models.IntegerField(
        choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_cat", on_delete=models.CASCADE)
    is_tab = models.BooleanField(
        default=False, verbose_name="是否导航", help_text="是否导航")

    class Meta:
        # abstract: 抽象
        abstract = True  # 说明是抽象模型类, 用于继承使用，数据库迁移时不会创建BaseModel的表
