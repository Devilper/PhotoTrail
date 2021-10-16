from django.db import models


# Create your models here.

class PersonInfoModel(models.Model):
    phone = models.CharField(max_length=11, verbose_name="手机号", unique=True)
    passwd = models.CharField(max_length=128, verbose_name="密码")
    nick_name = models.CharField(max_length=32, verbose_name="昵称", unique=True)
    location = models.CharField(max_length=32, verbose_name="位置")
    photos = models.IntegerField(verbose_name="照片数量")
    register_time = models.DateTimeField(auto_now=True, verbose_name="注册时间")
    last_time = models.DateTimeField(auto_now_add=True, verbose_name="最后登陆时间")
    is_delete = models.BooleanField(default=0, verbose_name="是否删除")

    class Meta:
        db_name = "person_info"
        verbose_name = "个人信息"
