from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from extensions.utils import jalali_converter, jalali_converter_2


#-----------> Managers Start
class ArticleManager(models.Manager):
    def published(self):
        dic = {}
        articles = Article.objects.filter(status = 'p').order_by('-publish')
        for article in articles:
            list_category =[]
            cats = Article.objects.get(slug = article.slug).category.all()
            for cat in cats:
                list_category.append(cat)
            dic[article]= list_category

        return dic

    def drafted(self):
        return self.filter(status = 'p')
    
    def last_3_published(self):
        return self.filter(status = 'p')[:3]

    def categories(self,slug):   #### TODO Change this method on another Objects
        titles = []
        items = self.get(slug = slug).category.all()
        for item in items:
            titles.append(item.title)
        return titles 


    def comments(self, article):
            dic = {}
            CMs =  Comments.objects.filter(article=article)
            for CM in CMs :
                dic[CM]= Comments_Answer.objects.filter(comment=CM)
            return dic

    def replys(self, cm):
        return Comments_Answer.objects.filter(comment=cm)

    def comment_count(self, article):

            cms = Comments.objects.filter(article=article)
            cm_count = int(Comments.objects.filter(article=article).count())
            for cm in cms:
                cm_count = cm_count + int(Comments_Answer.objects.filter(comment=cm).count())
            return cm_count


class CategoryManager(models.Manager):
    def published(self):
        return self.filter(status = 'p')
    def drafted(self):
        return self.exclude(status = 'p')


class CommentsManager(models.Manager):
    def get_comment_article(self):
        pass
    def get_comment_reply(self):
        pass
#-----------> Managers End




#-----------> Models Start

#  Category Model DataBase (Many to Many for Artticle)
class Category(models.Model):
    title = models.CharField(max_length=200 ,verbose_name="عنوان")
    slug = models.SlugField(max_length=100 ,unique=True,allow_unicode=True,verbose_name="اسلاگ")
    status = models.BooleanField(default=True ,verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")
    class Meta :
        verbose_name = "دسته بندی"
        verbose_name_plural= "دسته بند  ها"
        ordering = ['position']

    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title

# Article  Model DataBase (Many to Many to Category)(ForeignKey to User)
class Article(models.Model):
    STATUS_CHOICES = (
        ('d','پیش نویس'),
        ('p', 'منتشر شده'),
    )
    title = models.CharField(max_length=200 ,verbose_name="عنوان")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1,verbose_name="نویسنده")
    slug = models.SlugField(max_length=100 ,allow_unicode=True,unique=True,verbose_name="اسلاگ")
    description = models.TextField(default=None,verbose_name="توضیحات")
    thumbnail = models.ImageField(upload_to="images",verbose_name="تصویر")
    category = models.ManyToManyField(Category,verbose_name="دسته بندی ")
    publish = models.DateTimeField(default=timezone.now,verbose_name="تاریخ انتشار")
    created = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ایجاد")
    updated = models.DateTimeField(auto_now = True,verbose_name="تاریخ بروز رسانی")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,verbose_name="وضعیت")


    objects = ArticleManager()

    class Meta :
        verbose_name = "مقاله"
        verbose_name_plural= "مقاله ها"

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)

    def jcreated(self):
        return jalali_converter(self.created)

    def jupdated(self):
        return jalali_converter(self.updated)

    def jday(self):
        day, month, year = jalali_converter_2(self.publish)
        return day

    def jmonth(self):
        year, month, day = jalali_converter_2(self.publish)
        return month
        
    def short_des(self):
        return self.description[:100]+"......."



# Comments  Model DataBase (ForeignKey to article)

class Comments(models.Model):
    name = models.CharField(max_length=200 ,verbose_name="نام")
    email = models.CharField(max_length=100, default=None,verbose_name="ایمیل")
    text = models.TextField(default=None,verbose_name="نظر")
    date = models.DateTimeField(default=timezone.now,verbose_name="تاریخ انتشار")
    status = models.BooleanField(default=True ,verbose_name="آیا نمایش داده شود؟")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله مرتبط')
    class Meta :
        verbose_name = "نظر اصلی"
        verbose_name_plural= "نظرات اصلی"
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
    def jpublish(self):
        return jalali_converter(self.date)

# Comments_Answer  Model DataBase (ForeignKey to article)(ForeignKey to Comments)

class Comments_Answer(models.Model):
    name = models.CharField(max_length=200 ,verbose_name="نام")
    email = models.CharField(max_length=100, default=None,verbose_name="ایمیل")
    text = models.TextField(default=None,verbose_name="نظر")
    date = models.DateTimeField(default=timezone.now,verbose_name="تاریخ انتشار")
    status = models.BooleanField(default=True ,verbose_name="آیا نمایش داده شود؟")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله مرتبط')
    comment =models.ForeignKey(Comments, on_delete=models.CASCADE, verbose_name='نظر مرتبط')

    class Meta :
        verbose_name = "پاسخ نظر"
        verbose_name_plural= "پاسخ های نظرات"

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
    def jpublish(self):
        return jalali_converter(self.date)



#-----------> Models Ends