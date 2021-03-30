from django.contrib import admin
from .models import *

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('project','title','amount','user','jpub_date')
    list_filter= ('user', 'project', 'category_pay')
    search_fields = ('title','description')

class ExpenceAdmin(admin.ModelAdmin):
    list_display = ('project','title','amount','user','jpub_date')
    list_filter = ('user', 'project', 'category_pay')
    search_fields = ('title','description')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','address','Manager')
    search_fields = ('name', 'address')

admin.site.register(income,IncomeAdmin)
admin.site.register(expence,ExpenceAdmin)
admin.site.register(ProjectModel,ProjectAdmin)

