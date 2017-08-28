from .models import Source, NewsFeed, Contact
import datetime, threading, time
from .crawlers.notice import college, credit, event, lesson, notice, scholarship
from .crawlers.info import info, manage, welfare_student
from .crawlers import academic_calendar, menu, skhu, weather
from django.dispatch import receiver
from django.core.signals import request_started

pulltime = datetime.datetime.utcnow()

@receiver(request_started)
def http_req_started(sender, **kwargs):
    ## When receiving http request start event
    global pulltime
    now = datetime.datetime.utcnow()
    if ( now > pulltime):
        t = threading.Thread(target=run_crawler)
        t.daemon = True
        t.start()
        pulltime = now + datetime.timedelta(hour=1)


def run_crawler():
    while True:
        print("Running Crawling tasks")
        contactList = [info.run(), manage.run(), welfare_student.run()]
        print(contactList)
        for group in contactList:
            for item in group:
                contact, created = Contact.objects.get_or_create(
                    name = item['name'],
                    desc = item['class'] + item['task'] + item['fax'],
                    phone = item['phone']
                )
                contact.save()

        feedsList = [college.run(), credit.run(), event.run(), lesson.run(), notice.run(), scholarship.run()]
        print(feedsList)
        for main in feedsList:
            data = main['data']
            srcDic = main['source']
            print(srcDic)
            for item in data:
                source, created = Source.objects.get_or_create(url=srcDic['url'])
                source.name = srcDic['name']
                source.desc = srcDic['desc']
                source.save()

                NewsFeed.objects.get_or_create(
                    source=source,
                    title = item['title'],
                    summary ="",
                    url = item['url']
                )


# list3 = [academic_calendar.run(), menu.run(), weather.run()]
# print(list3)
