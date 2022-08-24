from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

class UserExtension(models.Model):
    # 与User模型构成一对一关系
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='extension')
    # 添加用户生日
    birthday = models.DateField(null=True,blank=True)
    # 添加用户手机号
    phone = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return self.user.username
    
 
# 信号接受函数,每当新建User实例时自动调用
@receiver(post_save, sender=User)
def create_user_extension(sender, instance, created, **kwargs):
    if created:
        UserExtension.objects.create(user=instance)
    else:
        instance.extension.save()