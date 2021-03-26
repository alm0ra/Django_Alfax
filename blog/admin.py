from django.contrib import admin
from .models import *
from django.utils.translation import ngettext
from django.contrib import messages


def show(modeladmin, request, queryset):
        updated = queryset.update(status=True)
        modeladmin.message_user(request, ngettext(
            '%d   نمایش داده شد.',
            '%d   نمایش داده شدند.',
            updated,
        ) % updated, messages.SUCCESS)
show.short_description = "نمایش دادن"

def hide(modeladmin, request, queryset):
        updated = queryset.update(status=False)
        modeladmin.message_user(request, ngettext(
            '%d    پنهان شد.',
            '%d    پنهان شدند.',
            updated,
        ) % updated, messages.SUCCESS)
hide.short_description = "نمایش داده نشوند"

def make_drafted(modeladmin, request, queryset):
        updated = queryset.update(status='d')
        modeladmin.message_user(request, ngettext(
            '%d مقاله پیش نویس شد.',
            '%d مقالات پیش نویس شدند.',
            updated,
        ) % updated, messages.SUCCESS)

make_drafted.short_description = "منتشر کردن مقالات"


def make_published(modeladmin, request, queryset):
        updated = queryset.update(status='p')
        modeladmin.message_user(request, ngettext(
            '%d مقاله منتشر شد.',
            '%d مقالات منتشر شدند.',
            updated,
        ) % updated, messages.SUCCESS)

make_published.short_description = "منتشر کردن مقالات"


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','jpublish','status','category_to_str')
    list_filter = ('author','publish','status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug':('title',)}
    ordering = ['-status', 'publish']
    actions = [make_published,make_drafted]

    def category_to_str(self , obj):
        return ", ".join([cat.title for cat in Category.objects.all()])
    category_to_str.short_description = "تگ ها"


admin.site.register(Article,ArticleAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title','slug','status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug':('title',)}
    actions = [show,hide]

admin.site.register(Category,CategoryAdmin)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name','text','article','status')
    list_filter = (['status'])
    search_fields = ('name', 'text')
    actions = [show,hide]

admin.site.register(Comments,CommentsAdmin)

class Comments_AnswerAdmin(admin.ModelAdmin):
    list_display = ('name','text','article','comment','status')
    list_filter = (['status'])
    search_fields = ('name', 'text')
    actions = [show,hide]

admin.site.register(Comments_Answer,Comments_AnswerAdmin)