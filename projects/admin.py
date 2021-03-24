from django.contrib import admin
from .models import *

class Skill_categoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug','status')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug':('title',)}
    ordering = ['-status']
    
admin.site.register(Skills_category,Skill_categoryAdmin)

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('project_title','project_address','project_subject','status')
    list_filter = ('publish_date','status')
    search_fields = ('project_title', 'project_description')
    prepopulated_fields = {'project_slug':('project_title',)}
    ordering = ['-status', 'publish_date']
    
admin.site.register(Projects_detail,ProjectsAdmin)