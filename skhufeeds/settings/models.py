from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    last_pull = models.DateTimeField(auto_now_add=False, auto_now=False)
    token = models.TextField()
    last_command = models.CharField(max_length=10, null=True)
#
# 사용자 구독정보 모델
class SubscribeList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source_id = models.ForeignKey('crawlers.Sources', on_delete = models.CASCADE)
