from django.db import models

#Create your models here.
#크롤링 데이터 분류를 위한 모델
class Source(models.Model):
    name = models.CharField(max_length=45)
    url = models.URLField()
    desc = models.TextField()

#피드 데이터 모델
class NewsFeed(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length = 45)
    summary = models.CharField(max_length = 100)
    url = models.URLField()
    source = models.ForeignKey(
        Source,
        on_delete = models.PROTECT
    )

#연락처 데이터 모델
class Contact(models.Model):
    name = models.CharField(max_length = 45)
    desc = models.TextField()
    phone = models.CharField(max_length = 45)
    email = models.EmailField()

    def __str__(self):
        return "{} : {} <{} / {}>".format(self.id, self.name, self.phone, self.email)

class Diet(models.Model):
    date = models.DateTimeField()
    lunchA = models.TextField()
    lunchB = models.TextField()
    dinner = models.TextField()
