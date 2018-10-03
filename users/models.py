from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    GENDER_CHOICES = (
        (1, '男'),
        (2, '女'),
        (0, '未知'),
    )
    nickname = models.CharField(verbose_name='昵称', max_length=24, default='')
    mobile = models.CharField(verbose_name='电话', max_length=11, null=True, blank=True)
    email = models.EmailField(verbose_name='邮箱', null=True, blank=True)

    class Meta:
        db_table = 't_user_info'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
