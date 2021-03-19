from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','publish','status')
    list_filter = ('author','publish','status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug':('title',)}
    ordering = ['-status', 'publish']

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('title','amount','user','pub_date')
    list_filter = ('user','pub_date')
    search_fields= ('title', 'description')

class ExpenceAdmin(admin.ModelAdmin):
    list_display = ('title','amount','user','pub_date')
    list_filter = ('user','pub_date')
    search_fields= ('title', 'description')

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('nameandfamily','companyname','mobile','phone','address')
    list_filter = ('nameandfamily','companyname','mobile','phone','address')
    search_fields = ('nameandfamily','companyname','mobile','phone','address')


admin.site.register(invoice)
admin.site.register(Contacts,ContactsAdmin)
admin.site.register(income,IncomeAdmin)
admin.site.register(expence,ExpenceAdmin)
admin.site.register(buy)
admin.site.register(sell)
admin.site.register(UserProfile)
admin.site.register(Article,ArticleAdmin)
admin.site.register(test)