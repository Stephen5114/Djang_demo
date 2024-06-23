from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField('用户名', max_length=30,null=True,blank=True,unique=True)
    password = models.CharField('密码',max_length=30)
    email = models.EmailField('邮箱',null=True,blank=True,unique=True)