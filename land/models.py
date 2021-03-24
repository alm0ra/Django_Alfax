from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter, jalali_converter_2






#### -------------> Landing Page DB Start

class section1(models.Model):
    webtitle = models.CharField(max_length=50,verbose_name="تیتر وبسایت")
    logoheader = models.ImageField(upload_to="user_avatar",verbose_name="لوگو هدر ۸۰*۴۰")
    text11 = models.CharField(max_length=50,verbose_name="متن ثابت قسمت ۱")
    text12 = models.CharField(max_length=50,verbose_name="متن انیمیشن ۱")
    text13 = models.CharField(max_length=50,verbose_name="متن انیمیشن ۲")
    text14 = models.CharField(max_length=50,verbose_name="متن ثابت")
    text15 = models.CharField(max_length=50,verbose_name="متن دکمه ")
    link15 = models.CharField(max_length=200,verbose_name="لینک دکمه")
    class Meta:
        verbose_name= "تنظیم قسمت ۱"
        verbose_name_plural = "--DONT TOUCH--"

class section2(models.Model):
    text21 = models.CharField(max_length=50,verbose_name=" متن ثابت قسمت ۲")
    text22 = models.CharField(max_length=50,verbose_name="متن ثابت")
    text23 = models.CharField(max_length=50,verbose_name="متن دکمه ")
    link23 = models.CharField(max_length=200,verbose_name="لینک دکمه")
    class Meta:
        verbose_name= "تنظیم  قسمت ۲"
        verbose_name_plural = "--DONT TOUCH--"

class section3(models.Model):
    text31 = models.CharField(max_length=50,verbose_name=" تیتر قسمت ۳")
    titr31 = models.CharField(max_length=50,verbose_name="متن قسمت ۳")

    text32 = models.CharField(max_length=50,verbose_name=" تیتر آیکون ۱")
    titr32 = models.CharField(max_length=50,verbose_name="متن آیکون ۱")

    text33 = models.CharField(max_length=50,verbose_name=" تیتر آیکون 2")
    titr33 = models.CharField(max_length=50,verbose_name="متن آیکون 2")

    text34 = models.CharField(max_length=50,verbose_name=" تیتر آیکون 3")
    titr34 = models.CharField(max_length=50,verbose_name="متن آیکون 3")

    text35 = models.CharField(max_length=50,verbose_name=" تیتر آیکون 4")
    titr35 = models.CharField(max_length=50,verbose_name="متن آیکون 4")
    class Meta:
        verbose_name= "تنظیم  قسمت ۳"
        verbose_name_plural = "--DONT TOUCH--"

class footer(models.Model):
    titr1 =models.CharField(max_length=50,verbose_name=" تیتر فوتر ")
    text1 = models.CharField(max_length=50,verbose_name=" تیتر زیر تیتر ")

    text00 =models.CharField(max_length=50,verbose_name="متن دکمه")
    link00 = models.CharField(max_length=200,verbose_name="لینک دکمه")

    text11 =models.CharField(max_length=50,verbose_name="متن لینک ۱")
    link11 = models.CharField(max_length=50,verbose_name=" لینک ۱")

    text22 = models.CharField(max_length=50,verbose_name="متن لینک ۲")
    link22 = models.CharField(max_length=50,verbose_name=" لینک ۲")

    text33 = models.CharField(max_length=50,verbose_name="متن لینک ۳")
    link33 = models.CharField(max_length=50,verbose_name=" لینک ۳")

    address =  models.CharField(max_length=50,verbose_name="آدرس در فوتر")
    phone =  models.CharField(max_length=50,verbose_name="تلفن در فوتر")
    mail=  models.CharField(max_length=50,verbose_name="ایمیل در فوتر")
    class Meta:
        verbose_name= "تنظیم  فوتر"
        verbose_name_plural = "--DONT TOUCH--"

class LandingPage(models.Model):
    fisrt_section = models.ForeignKey(section1, on_delete=models.CASCADE, verbose_name='تنظیمات قسمت ۱ صفحه اصلی')
    section_section = models.ForeignKey(section2, on_delete=models.CASCADE, verbose_name='تنظیمات قسمت ۲ صفحه اصلی')
    third_section = models.ForeignKey(section3, on_delete=models.CASCADE, verbose_name='تنظیمات قسمت ۳ صفحه اصلی')
    footer_section = models.ForeignKey(footer, on_delete=models.CASCADE, verbose_name='تنظیمات فوتر  صفحه اصلی' )
    
    class Meta :
        verbose_name = "تنظیمات صفحه اصلی"
        verbose_name_plural= "تنظیمات صفحه اصلی"


#### -------------> Landing Page DB End

#### -------------> Resume Page DB End

class Header(models.Model):
    name_text = models.CharField(max_length=50,verbose_name=" نام و نام خانوادگی")
    title_text = models.CharField(max_length=50,verbose_name=" سمت یا شغل یا حرفه")
    text1 = models.CharField(max_length=50,verbose_name=" توضیحات ۱")
    text2 = models.CharField(max_length=50,verbose_name=" توضیححات ۲")
    last_act = models.CharField(max_length=50,verbose_name=" فعالیت قبلی")
    edu_text = models.CharField(max_length=50,verbose_name=" تحصیلات")
    profile_pic = models.ImageField(upload_to="user_avatar",verbose_name="عکس پروفایل با ابعاد ۴۶۰×۳۴۰")

    class Meta:
        verbose_name=  "تنظیمات  هدر قسمت ۱"
        verbose_name_plural = "--DONT TOUCH--"

class Aboutme(models.Model):
    description = models.TextField(default=None,verbose_name="توضیحات")
    birthdate = models.CharField(max_length=100, verbose_name="تاریخ تولد شمسی")
    married_status=models.CharField(max_length=50, verbose_name="وضعیت تاهل :")
    nationality = models.CharField(max_length=30, verbose_name="ملیت")
    tel_id = models.CharField(max_length=30, verbose_name="آیدی تلگرام")
    phone = models.CharField(max_length=30, verbose_name="تلفن")
    mail = models.CharField(max_length=30, verbose_name="ایمیل")

    class Meta:
        verbose_name=  "تنظیمات درباره من"
        verbose_name_plural = "--DONT TOUCH--"

    # class Meta :
    #     verbose_name = "تنظیمات درباره من"
    #     verbose_name_plural=  "تنظیمات درباره من"

class My_exprience(models.Model):
    from_date = models.CharField(max_length=30, verbose_name="از تاریخ")
    untill_date = models.CharField(max_length=30, verbose_name="تا تاریخ")
    Length_date = models.CharField(max_length=30, verbose_name="مدت زمانی که اونجا بودی")
    company_name = models.CharField(max_length=30, verbose_name=" نام شرکتی که توش بودی")
    city_name = models.CharField(max_length=30, verbose_name="نام شهر شرکت")
    job_title = models.CharField(max_length=30, verbose_name="تیتر شغلی که ذاشتی")
    text = models.TextField(default=None,verbose_name="توضیحات")

    class Meta:
        verbose_name= "تنظیمات تجربیات من"
        verbose_name_plural = "--DONT TOUCH--"
    # class Meta :
    #     verbose_name = "تنظیمات تجربیات من"
    #     verbose_name_plural=  "تنظیمات تجربیات من"

class  Education(models.Model):
    ed_title = models.CharField(max_length=30, verbose_name="نام موسسه")
    ed_situation = models.CharField(max_length=30, verbose_name="موقعیت تحصیلی یا رشته")
    year1 = models.CharField(max_length=30, verbose_name="سال شروع")
    year2 = models.CharField(max_length=30, verbose_name="سال پایان")

    class Meta:
        verbose_name= "تنظیمات تحصیلات من"
        verbose_name_plural = "--DONT TOUCH--"

    # class Meta :
    #     verbose_name = "تنظیمات تحصیلات من"
    #     verbose_name_plural=  "تنظیمات تحصیلات من"

class Skill_part1(models.Model):
    skill_name = models.CharField(max_length=30, verbose_name="نام توانایی ")
    skill_percent = models.IntegerField(verbose_name="درصد توانایی")

    class Meta:
        verbose_name= "توانایی های قسمت چپ"
        verbose_name_plural = "--DONT TOUCH--"
    # class Meta :
    #         verbose_name ="توانایی های قسمت چپ"
    #         verbose_name_plural=  "توانایی های قسمت چپ"

class Skill_part2(models.Model):
    skill_name = models.CharField(max_length=30, verbose_name="نام توانایی ")
    skill_percent = models.IntegerField( verbose_name="درصد توانایی")

    class Meta:
        verbose_name= "توانایی های سمت راست"
        verbose_name_plural = "--DONT TOUCH--"

    # class Meta :
    #         verbose_name = "توانایی های سمت راست"
    #         verbose_name_plural= "توانایی های سمت راست"

class Skills(models.Model):
    skill_part1 = models.ForeignKey(Skill_part1, on_delete=models.CASCADE, verbose_name="توانایی های قسمت چپ")
    skill_part2 = models.ForeignKey(Skill_part2, on_delete=models.CASCADE, verbose_name="توانایی های سمت راست")

    class Meta:
        verbose_name= "تنظیم توانایی ها"
        verbose_name_plural = "--DONT TOUCH--"


class ResumePage(models.Model):
    header = models.ForeignKey(Header, on_delete=models.CASCADE, verbose_name="تنظیمات هدر")
    aboutme = models.ForeignKey(Aboutme, on_delete=models.CASCADE, verbose_name="تنظیمات قسمت درباره ")
    my_exprience = models.ForeignKey(My_exprience, on_delete=models.CASCADE, verbose_name="تنظیمات قسمت تجربیات ")
    education = models.ForeignKey(Education, on_delete=models.CASCADE, verbose_name="تنظیمات قسمت تحصیلات من")
    skills = models.ForeignKey(Skill_part2, on_delete=models.CASCADE, verbose_name="تنظیمات توانایی های من")
    class Meta:
        verbose_name = "تنظیمات صفحه رزومه"
        verbose_name_plural = "تنظیمات صفحه رزومه"

