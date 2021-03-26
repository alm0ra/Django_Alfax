from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from extensions.utils import jalali_converter







class project(models.Model):
    METHOD_CHOICE = (
        ('a','در حال انجام'),
        ('b','پایان یافته'),
    )

    name= models.CharField(max_length=100,verbose_name="نام پروژه") 
    zirbana = models.IntegerField(verbose_name="مساحت زیر بنا متر مربع")
    tedad_tabaqat = models.IntegerField(verbose_name="تعداد طبقات پروژه")
    address = models.CharField(max_length=150 ,blank=True, null=True , verbose_name="آددرس پروژه")
    Members = models.ManyToManyField(User, related_name='member',verbose_name="انتخاب شرکا")
    Manager = models.ForeignKey(User,related_name='manager' ,on_delete=models.CASCADE, verbose_name="مدیر پروژه")
    description = models.TextField(max_length=400 , verbose_name="توضیحات پروژه",blank=True)
    project_status = models.CharField(max_length=1,choices=METHOD_CHOICE, verbose_name="وضعیت پروژه" )
    created_date = models.DateField(auto_now_add=True, verbose_name= "تاریخ ایجاد پروژه")
    
    class Meta :
        verbose_name = "پروژه عمرانی"
        verbose_name_plural= "پروژه های عمرانی"
        
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name


class income(models.Model):
    METHOD_CHOICES = (
        ('n', 'نقد'),
        ('c','چک'),
    )
    CATEGORY_CHOICES = (
        ('a','تامین مالی از مالک'),
        ('b','فروش آهن آلات'),
        ('c','فروش ملک'),
        ('d','سایر'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name="هزینه شده توسط ")
    project = models.ForeignKey(project, on_delete=models.CASCADE, verbose_name="پروژه مربوطه")
    title = models.CharField(max_length=200,verbose_name="عنوان هزینه کرد")
    amount = models.BigIntegerField(verbose_name="مقدار هزینه")
    description = models.TextField(max_length=200, blank=True, null=True,verbose_name="توضیحات")
    pay_mehod = models.CharField(max_length=1, choices=METHOD_CHOICES,verbose_name="شیوه پرداخت")
    category_pay = models.CharField(max_length=1, choices=CATEGORY_CHOICES, verbose_name="از کدام منبع درآمد داشتید")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ انتشار")


    class Meta :
        verbose_name = "درآمد"
        verbose_name_plural= "درآمد ها"
        
    def __str__(self):
        return "{} - {}".format(self.title,self.amount)
    def __unicode__(self):
        return "{} - {}".format(self.title,self.amount)

    def jpub_date(self):
        return jalali_converter(self.pub_date)


class expence(models.Model):
    METHOD_CHOICES = (
        ('n', 'نقد'),
        ('c','چک'),
    )
    CATEGORY_CHOICE = (
        ('a','صدور پروانه'),
        ('b','شهرداری'),
        ('c','آرماتور بند'),
        ('d','شرکت بتن'),
        ('e','آهن آلات'),
        ('f','تاسیسات'),
        ('g','مصالح'),
        ('i','دستمزد کارگر بنا'),
        ('j','تخریب'),
        ('k','آب و برق و گاز'),
        ('l','کرایه تجهیزات'),
        ('m','متفرقه'),

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name="هزینه شده توسط ")
    project = models.ForeignKey(project, on_delete=models.CASCADE, verbose_name="پروژه مربوطه")
    title = models.CharField(max_length=200,verbose_name="عنوان")
    amount = models.BigIntegerField(verbose_name="مقدار هزینه کرد به تومان")
    description = models.TextField(max_length=200, blank=True, null=True,verbose_name="توضیحات")
    pay_mehod = models.CharField(max_length=1, choices=METHOD_CHOICES,verbose_name="شیوه پرداخت")
    category_pay = models.CharField(max_length=1, choices=CATEGORY_CHOICE, verbose_name="در کدام شاخه هزینه کردید")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ انتشار")


    class Meta :
        verbose_name = "هزینه کرد"
        verbose_name_plural= " هزینه کرد ها"
        
    def __str__(self):
        return "{} - {}".format(self.title,self.amount)
    def __unicode__(self):
        return "{} - {}".format(self.title,self.amount)

    def jpub_date(self):
        return jalali_converter(self.pub_date)
