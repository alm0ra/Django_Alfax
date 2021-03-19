from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Article(models.Model):
    STATUS_CHOICES = (
        ('d','Draft'),
        ('p', 'Published'),
    )
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    slug = models.CharField(max_length=100 ,unique=True)
    description = models.TextField(default=None)
    thumbnail = models.ImageField(upload_to="images")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.slug
    def __unicode__(self):
        return self.slug

class UserProfile(models.Model):
    avatar = models.ImageField(upload_to="user_avatar")
    address = models.CharField(max_length=100)
    postalcode = models.CharField(max_length=20)
    startregister = models.DateTimeField(default=timezone.now)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.user.username
    def __unicode__(self):
        return self.user.username

class test(models.Model):
    avatar = models.ImageField(upload_to="user_avatar")
    address = models.CharField(max_length=100)
    postalcode = models.CharField(max_length=20)
    startregister = models.DateTimeField(default=timezone.now)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.user.username
    def __unicode__(self):
        return self.user.username


class Contacts(models.Model):
    nameandfamily = models.CharField(max_length=50)
    companyname = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=50,blank=True)
    phone = models.CharField(max_length=50,blank=True)
    address = models.CharField(max_length=50,blank=True)
    email = models.CharField(max_length=100, default=None)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nameandfamily
    def __unicode__(self):
        return self.nameandfamily


class income(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "{} - {}".format(self.title,self.amount)
    def __unicode__(self):
        return "{} - {}".format(self.title,self.amount)

class expence(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    pub_date = models.DateTimeField()

    def __str__(self):
        return "{} - {}".format(self.title,self.amount)
    def __unicode__(self):
        return "{} - {}".format(self.title,self.amount)






class invoice(models.Model):
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    system_type = (
        ('D', 'Direct'),
        ('I', 'Indirect'),
        ('T', 'Telescopic'),
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