from django.contrib import admin
from . import models


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_on')
    search_fields = ['name', 'email']
    ordering = ['-name']
    list_filter = ['active']
    date_hierarchy = 'created_on'

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author', 'category',)
    search_fields = ['title', 'content']
    ordering = ['-pub_date']
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'    


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name',)   


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name',)

# Register your models here.
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Author ,AuthorAdmin)
admin.site.register(models.Category , CategoryAdmin)
admin.site.register(models.Tag , TagAdmin)


