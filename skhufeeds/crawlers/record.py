from .models import Source, NewsFeed, Contact
import datetime
import threading
import time
from .crawlers.notice import college, credit, event, lesson, notice, scholarship
from .crawlers.info import info, manage, welfare_student
from .crawlers import academic_calendar, menu, skhu, weather
from django.dispatch import receiver
from django.core.signals import request_started
from celery import shared_task
from pyshorteners import Shortener
# # When database is ready

pulltime = datetime.datetime.utcnow()

@receiver(request_started)
def db_connected(sender, **kwargs):
    global pulltime
    time_now = datetime.datetime.utcnow()
    if(time_now > pulltime):
        run_crawler.apply_async(countdown=5)
        pulltime = datetime.datetime.utcnow() + datetime.timedelta(hours=1)


@shared_task  # This function will ran asynchronously via Celery
def run_crawler():
    shortener = Shortener('Tinyurl')
    print("Running Crawling tasks")
    contactList = [info.run(), manage.run(), welfare_student.run()]
    print(contactList)
    for group in contactList:
        for item in group:
            contact, created = Contact.objects.get_or_create(
                name=item['name'],
                desc=item['class'] + item['task'] + item['fax'],
                phone=item['phone']
            )
            contact.save()

    feedsList = [college.run(), credit.run(), event.run(),
                 lesson.run(), notice.run(), scholarship.run()]
    print(feedsList)
    for main in feedsList:
        data = main['data']
        srcDic = main['source']
        print(srcDic)
        for item in data:
            shorturl = shortener.short(srcDic['url'])
            source, created = Source.objects.get_or_create(url=shorturl)
            source.name = srcDic['name']
            source.desc = srcDic['desc']
            source.save()

            NewsFeed.objects.get_or_create(
                source=source,
                title=item['title'],
                summary="",
                url=item['url']
            )
    print("Task DONE!")


# list3 = [academic_calendar.run(), menu.run(), weather.run()]
# print(list3)
