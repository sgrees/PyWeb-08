from django.contrib import admin

from myblog.models import Category
from myblog.models import Post


class Category_Inline(admin.TabularInline):
    model = Category.posts.through

class Category_Admin(admin.ModelAdmin):
    inlines = [Category_Inline]
    exclude = ('posts',)

class Post_Admin(admin.ModelAdmin):
    inlines = [Category_Inline]

admin.site.register(Category, Category_Admin)
admin.site.register(Post, Post_Admin)
