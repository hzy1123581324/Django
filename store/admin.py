from django.contrib import admin

from store.models import GoodsCategory, Commodity

# Register your models here.
admin.site.register(Commodity)
admin.site.register(GoodsCategory)
