from django.contrib import admin
from catalog.models import Product,Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    search_fields = ('name','description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','price', 'category',)
    list_filter = ('category','description',)
    search_fields = ('name',)

