from .models import Source, NewsFeed, Contact
import datetime
from .crawlers.notice import college, credit, event, lesson, notice, scholarship
from .crawlers.info import info, manage, welfare_student
from .crawlers import academic_calendar, menu, skhu, weather
from background_task import background
from django.dispatch import receiver
from django.db.backends.signals import connection_created

def db_connected(sender, connection, **kwargs):
    #repeat crawling task for every hour
    print("DB Connection Ready.")
    run_crawler(repeat=3600)

# DB connect event
connection_created.connect(db_connected)

@background(schedule=10)
def run_crawler():
    print("Running Crawling tasks")
    contactList = [info.run(), manage.run(), welfare_student.run()]
    print(contactList)
    for group in contactList:
        for item in group:
            contact, created = Contact.objects.get_or_create(
                name=item['name'],
                desc = item['class'] + item['task'] + item['fax'],
                phone = item['phone']
            )
            contact.save()

    feedsList = [college.run(), credit.run(), event.run(), lesson.run(), notice.run(), scholarship.run()]
    print(feedsList)
    for main in feedsList:
        data = main['data']
        srcDic = main['source']
        for item in data:
            source = Source.objects.get_or_create(url=srcDic['url'])
            source.name = srcDic['name']
            source.desc = srcDic['desc']
            source.save()

            feed, created = NewsFeed.objects.get_or_create(
                source=source,
                title = item['title'],
                summary ="",
                url = item['link']
            )
            feed.save()


# list3 = [academic_calendar.run(), menu.run(), weather.run()]
# print(list3)
