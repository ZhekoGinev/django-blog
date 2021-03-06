from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'content', 'created_on']


admin.site.register(Article, ArticleAdmin)