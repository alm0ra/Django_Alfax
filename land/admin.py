from django.contrib import admin
from .models import *




class Skill_categoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug','status')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug':('title',)}
    ordering = ['-status']
    
admin.site.register(Skill_category,Skill_categoryAdmin)

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('project_title','project_address','project_subject','status')
    list_filter = ('publish_date','status')
    search_fields = ('project_title', 'project_description')
    prepopulated_fields = {'project_slug':('project_title',)}
    ordering = ['-status', 'publish_date']
    
admin.site.register(Projects,ProjectsAdmin)
admin.site.register(ResumePage)

admin.site.register(LandingPage)

admin.site.register(section1)
admin.site.register(section2)
admin.site.register(section3)
admin.site.register(footer)
admin.site.register(Header)
admin.site.register(Aboutme)
admin.site.register(My_exprience)
admin.site.register(Education)
admin.site.register(Skill_part1)
admin.site.register(Skill_part2)
admin.site.register(Skills)