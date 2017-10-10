from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from crawlers.models import Source


# Create your models here.

# class UserInfo(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     last_pull = models.DateTimeField(auto_now_add=False, auto_now=False)
#     token = models.TextField(default="")
#     secret = models.TextField(default="")
#     last_command = models.CharField(max_length=10, default="")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.TextField(blank=True) # Login token
    secret = models.TextField(blank=True) # Secret for JWT Encryption
    last_pull = models.DateTimeField(auto_now_add=True, null=True, blank=True) # Last pull date & time
    last_input = models.CharField(max_length=10, blank=True) # Last Input of the user

# Create user profile data on user registration
@receiver(post_save, sender=User)
def create_or_save_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


#
# 사용자 구독정보 모델
class Subscribed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 사용자 외래키
    source = models.ForeignKey(Source, on_delete = models.CASCADE) # 구독항목 외래키 

    # class Meta:
    #     unique_together = ('user', 'source')
