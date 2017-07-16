from django.db import models

# Create your models here.
# 사용자 데이터 모델
class Subscribers(models.Model):
    user_id = models.CharField(max_length=45)

# 사용자 구독정보 모델
class SubscribeList(models.Model):
    user_id = models.ForeignKey('Subscribers', on_delete = models.CASCADE)
    source_id = models.ForeignKey('crawlers.Sources', on_delete = models.CASCADE)
