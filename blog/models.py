from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from extensions.utils import jalali_converter

class Category(models.Model):
    title = models.CharField(max_length=200 ,verbose_name="عنوان")
    slug = models.CharField(max_length=100 ,unique=True,verbose_name="اسلاگ")
    status = models.BooleanField(default=True ,verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")
    class Meta :
        verbose_name = "دسته بندی"
        verbose_name_plural= "دسته بند  ها"
        ordering = ['position']

    def __str__(self):
        return self.title

class Article(models.Model):
    STATUS_CHOICES = (
        ('d','پیش نویس'),
        ('p', 'منتشر شده'),
    )
    title = models.CharField(max_length=200 ,verbose_name="عنوان")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1,verbose_name="نویسنده")
    slug = models.CharField(max_length=100 ,unique=True,verbose_name="اسلاگ")
    description = models.TextField(default=None,verbose_name="توضیحات")
    thumbnail = models.ImageField(upload_to="images",verbose_name="تصویر")
    category = models.ManyToManyField(Category,verbose_name="دسته بندی ")
    publish = models.DateTimeField(default=timezone.now,verbose_name="تاریخ انتشار")
    created = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ایجاد")
    updated = models.DateTimeField(auto_now = True,verbose_name="تاریخ بروز رسانی")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,verbose_name="وضعیت")
    class Meta :
        verbose_name = "مقاله"
        verbose_name_plural= "مقاله ها"

    def __str__(self):
        return self.slug
    def __unicode__(self):
        return self.slug
    def jpublish(self):
        return jalali_converter(self.publish)
    def jcreated(self):
        return jalali_converter(self.created)
    def jupdated(self):
        return jalali_converter(self.updated)