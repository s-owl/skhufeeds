from django.db import models

#Create your models here.
#크롤링 데이터 분류를 위한 모델
class Sources(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=45)
    url = models.UrlField()
    desc = models.TextField()

#피드 데이터 모델
class NewsFeeds(models.Model):
    id = models.AutoField()
    time = models.TimeField
    title = models.CharField(max_length = 45)
    summary = models.CharField(max_length = 100)
    url = models.UrlField
    source_id = models.ForeignKey(
        'Sources',
        on_delete = models.PROTECT,
    )

#연락처 데이터 모델
class Phone(models.Model)
    id = models.AutoField()
    name = models.CharField(max_length = 45)
    desc = models.TextField()
    phone = models.CharField(max_length = 45)
    email = models.EmailField()
