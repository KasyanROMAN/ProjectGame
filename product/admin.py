from django.contrib import admin

from product.models import Game

@admin.register(Game)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','link','description']
    search_fields = ['name']
