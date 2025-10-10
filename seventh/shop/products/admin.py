from django.contrib import admin
from .models import ProductCategory, Product, Photo


class PhotoAdd(admin.StackedInline):
    model = Photo
    fields = ('product', 'add_photo')
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoAdd]


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('product', 'add_photo')


admin.site.register(ProductCategory)
admin.site.register(Product, ProductAdmin)
admin.site.register(Photo, PhotoAdmin)
