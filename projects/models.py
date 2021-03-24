from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from extensions.utils import jalali_converter, jalali_converter_2

#### set up Manager 
class ProjectManager(models.Manager):
    def published(self):
        dic = {}
        projects = Projects_detail.objects.filter(status = 'p').order_by('-publish_date')
        for project in projects:
            list_category =[]
            cats = Projects_detail.objects.get(project_slug = project.slug).skillss_category.all()
            for cat in cats:
                list_category.append(cat)
            dic[project]= list_category

        return dic

    def categories(self,slug):   #### TODO Change this method on another Objects
        titles = []
        items = self.get(project_slug = slug).skillss_category.all()
        for item in items:
            titles.append(item.title)
        return titles 




#### -------------> Project Page DB start
class Skills_category(models.Model):
    title = models.CharField(max_length=200 ,verbose_name="عنوان")
    slug = models.SlugField(max_length=100 ,unique=True,allow_unicode=True,verbose_name="اسلاگ")
    status = models.BooleanField(default=True ,verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")

    class Meta :
        verbose_name = "دسته بندی پروژه"
        verbose_name_plural= "دسته بندی پروژه  بر اساس مهارت"
        ordering = ['position']

    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title


class Projects_detail(models.Model):

    STATUS_CHOICES = (
        ('d','پیش نویس'),
        ('p', 'منتشر شده'),
    )
    project_title = models.CharField(max_length=200 ,verbose_name="عنوان پروژه")
    project_customer = models.CharField(max_length=200, default=None ,verbose_name="سفارش دهنده یا مشتری پروژه")
    project_subject = models.CharField(max_length=200 ,verbose_name="موضوع پروژه یا توضیح کوتاه")
    project_slug = models.SlugField(max_length=100 ,unique=True,allow_unicode=True,verbose_name="اسلاگ پروژه")
    project_description = models.TextField(default=None,verbose_name="توضیحات")
    project_thumbnail = models.ImageField(upload_to="project_image",verbose_name="تصویر")
    project_address =  models.CharField(max_length=200 ,verbose_name="آدرس پروژه")
    skillss_category = models.ManyToManyField(Skills_category,verbose_name="دسته بندی پروژه بر اساس مهارت ")
    publish_date = models.DateTimeField(auto_now=True,verbose_name="تاریخ انتشار")
    start_date = models.DateTimeField(default=timezone.now,verbose_name="تاریخ شروع پروژه")
    end_date = models.DateTimeField(default=timezone.now,verbose_name="تاریخ  پایان پروژه")

    status = models.CharField(max_length=1, choices=STATUS_CHOICES,verbose_name="وضعیت")

    objects = ProjectManager()
    
    class Meta :
        verbose_name = "پروژه ها"
        verbose_name_plural= "پروژه ها"

    def __str__(self):
        return self.project_title
    def __unicode__(self):
        return self.project_title

    def jday(self):
        day, month, year = jalali_converter_2(self.end_date)
        return day

    def jmonth(self):
        day, month, year = jalali_converter_2(self.end_date)
        return month
        
    def jyear(self):
        day, month, year = jalali_converter_2(self.end_date)
        return year
#### -------------> Project Page DB End