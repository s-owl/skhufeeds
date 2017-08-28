from .models import Source, NewsFeed, Contact
import datetime, threading, time
from .crawlers.notice import college, credit, event, lesson, notice, scholarship
from .crawlers.info import info, manage, welfare_student
from .crawlers import academic_calendar, menu, skhu, weather
from django.dispatch import receiver
from django.db.backends.signals import connection_created


def db_connected(sender, connection, **kwargs):
    ## When DB connection is ready.
    print("DB Connection Ready.")
    t = threading.Thread(target=run_crawler)
    t.start()


# DB connect event
connection_created.connect(db_connected)

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
        # Run run_crawler again in an hour
        time.sleep(3600)


# list3 = [academic_calendar.run(), menu.run(), weather.run()]
# print(list3)
