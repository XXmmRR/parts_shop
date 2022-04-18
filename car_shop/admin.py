from django.contrib import admin
from .models import Mark, Model, Category, Part

# Register your models here.


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('mark_name',)
    search_fields = ('mark_name',)
    ordering = ('mark_name',)
    prepopulated_fields = {'mark_slug': ('mark_name',)}


@admin.register(Model)
class ModelsAdmin(admin.ModelAdmin):
    list_display = ('mark', 'model_name')
    search_fields = ('model_name', 'mark')
    ordering = ('mark',)
    prepopulated_fields = {'model_slug': ('model_name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('model', 'category_name')
    search_fields = ('model', 'category_name')
    ordering = ('model',)
    prepopulated_fields = {'category_slug': ('category_name',)}


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ('category', 'article', 'article_second', 'part_name', 'part_price')
    search_fields = ('category', 'article', 'article_second', 'part_name', 'part_price')
    ordering = ('part_name', 'part_price')
    prepopulated_fields = {'part_slug': ('part_name',)}

