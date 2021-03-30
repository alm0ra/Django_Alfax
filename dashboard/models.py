from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from extensions.utils import jalali_converter




class UserProfile(models.Model):
    avatar = models.ImageField(upload_to="user_avatar",verbose_name="تصویر پروفایل")
    address = models.CharField(max_length=100,verbose_name="آدرس")
    postalcode = models.CharField(max_length=20,verbose_name="کد پستی")
    startregister = models.DateTimeField(default=timezone.now,verbose_name="شروع عضویت")
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1,verbose_name="کاربر")
    class Meta :
        verbose_name = "پروفایل"
        verbose_name_plural= "پروفایل ها"

    def __str__(self):
        return self.user.username
    def __unicode__(self):
        return self.user.username
    



class Contacts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1, verbose_name="ثبت توسط")
    nameandfamily = models.CharField(max_length=50,verbose_name="نام و نام خانوادگی")
    companyname = models.CharField(max_length=50, blank=True,verbose_name="نام شرکت")
    mobile = models.CharField(max_length=50,unique=True,verbose_name="تلفن همراه")
    phone = models.CharField(max_length=50,unique=True,verbose_name="تلفن ثابت")
    address = models.CharField(max_length=50,blank=True,verbose_name="آدرس")
    email = models.CharField(max_length=100, default=None,verbose_name="ایمیل")
    created = models.DateTimeField(auto_now=True,verbose_name="ساخته شده در تاریخ ")
    class Meta :
        verbose_name = "مخاطبین"
        verbose_name_plural= "مخاطبین"

    def __str__(self):
        return self.nameandfamily
    def __unicode__(self):
        return self.nameandfamily
    def jcreated(self):
        return jalali_converter(self.created)



class invoice(models.Model):
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    system_type = (
        ('D', 'مستقیم'),
        ('I', 'غیر مستقیم'),
        ('T', 'تلسکوپی'),
    )
    slug = models.CharField(max_length=100 ,unique=True)
    invoicenumber= models.IntegerField()
    customername = models.CharField(max_length=30)
    projectname = models.CharField(max_length=30,null=True, blank=True, default=None)
    pub_date = models.DateTimeField()
    typeofsystem = models.CharField(max_length=3, choices=system_type ,default='I')
    travel = models.FloatField()
    weighthuman = models.IntegerField(null=True, blank=True, default=None)
    weightcaresling = models.IntegerField(null=True, blank=True, default=None)
    v = models.FloatField(null=True, blank=True, default=None)
    
    carsling = models.BooleanField(choices=BOOL_CHOICES, default=False)
    #---------------POWER---------------
    powerunit = models.BooleanField(choices=BOOL_CHOICES, default=False)
    motortype = models.CharField(max_length=30,null=True, blank=True, default=None)
    motorpower = models.FloatField(null=True, blank=True, default=None)
    typeofpomp= models.CharField(max_length=30,null=True, blank=True, default=None)
    pomplitr = models.IntegerField(null=True, blank=True, default=None)
    typeofvalve = models.CharField(max_length=30,null=True, blank=True, default=None)
    tanklitr = models.IntegerField(null=True, blank=True, default=None)
    oil = models.BooleanField(choices=BOOL_CHOICES, default=False)
    oirlitr = models.IntegerField(null=True, blank=True, default=None)
    shelang = models.BooleanField(choices=BOOL_CHOICES, default=False)
    shelangmeter = models.IntegerField(null=True, blank=True, default=None)
    oilheater = models.BooleanField(choices=BOOL_CHOICES, default=False)
    valverobgard = models.BooleanField(choices=BOOL_CHOICES, default=False)
    valveks = models.BooleanField(choices=BOOL_CHOICES, default=False)
    handpomp = models.BooleanField(choices=BOOL_CHOICES, default=False)
    rapcher = models.BooleanField(choices=BOOL_CHOICES, default=False)
    oilcolder = models.BooleanField(choices=BOOL_CHOICES, default=False)
    #----------------JACK-------------
    jack = models.BooleanField(choices=BOOL_CHOICES, default=False)
    flo = models.BooleanField(choices=BOOL_CHOICES, default=False)
    packingtype =  models.CharField(max_length=30,null=True, blank=True, default=None)
    typeofshaft = models.CharField(max_length=30,null=True, blank=True, default=None)
    shaftdiameter = models.IntegerField(null=True, blank=True, default=None)
    manisman = models.IntegerField(null=True, blank=True, default=None)
    jacksizeclose = models.FloatField(null=True, blank=True, default=None) 
    jackcorse = models.FloatField(null=True, blank=True, default=None)
    #-----------Tablobarq ---------
    Tablobarq = models.BooleanField(choices=BOOL_CHOICES, default=False)

    #------final-----
    price = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    class Meta :
        verbose_name = "فاکتور"
        verbose_name_plural= "فاکتور ها"
    def __str__(self):
        return str(self.invoicenumber)
    def __unicode__(self):
        return self.invoicenumber


class sell(models.Model):
    invoicenumber = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return "{} - {}".format(self.title,self.amount)
    def __str__(self):
        return "{} - {}".format(self.title,self.amount)
    class Meta :
        verbose_name = "فروش"
        verbose_name_plural= "فروش ها"

class buy(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    pub_date = models.DateTimeField()

    def __str__(self):
        return "{} - {}".format(self.title,self.amount)
    def __unicode__(self):
        return "{} - {}".format(self.title,self.amount)
    class Meta :
        verbose_name = "خرید"
        verbose_name_plural= "خرید ها"