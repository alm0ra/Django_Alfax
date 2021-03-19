from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','jpublish','status','category_to_str')
    list_filter = ('author','publish','status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug':('title',)}
    ordering = ['-status', 'publish']
    
    def category_to_str(self , obj):
        return ", ".join([cat.title for cat in Category.objects.all()])
    category_to_str.short_description = "تگ ها"


admin.site.register(Article,ArticleAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title','slug','status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Category,CategoryAdmin)