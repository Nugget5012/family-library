from django.contrib import admin
from .models import Manual, Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
  list_display = ("product_name", "product_model")

class ManualAdmin(admin.ModelAdmin):
  list_display = ("manual_title", "manual_url")

admin.site.register(Manual,ManualAdmin)
admin.site.register(Product,ProductAdmin)