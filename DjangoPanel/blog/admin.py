from django.contrib import admin
from blog.models import Category,Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'post_date')
    list_filter = ("title", "author", "category", "post_date")
    search_fields = ['title', 'author', 'category']
admin.site.register(Post, PostAdmin)