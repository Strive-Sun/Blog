from django.contrib import admin
from .models import Category, Post, Theme

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_time']
    search_fields = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'created_time', 'modified_time', 'views']
    list_filter = ['category', 'author', 'created_time']
    search_fields = ['title', 'content']
    date_hierarchy = 'created_time'

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_editable = ['is_active']
