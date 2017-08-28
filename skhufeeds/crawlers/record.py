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
    list1 = [info.run(), manage.run(), welfare_student.run()]
    print(list1)
    for group in list1:
        for item in group:
            contact = Contact.objects.get_or_create(
                name=item['name'],
                desc = item['class'] + item['task'] + item['fax'],
                phone = item['phone']
            )
            contact.save()

    list2 = [college.run(), credit.run(), event.run(), lesson.run(), notice.run(), scholarship.run()]
    print(list2)
    for main in list1:
        for item in main['data']:
            srcDic = main['source']
            source = get_or_create(url=srcDic['url'])
            source.name = srcDic['name']
            source.desc = srcDic['desc']
            source.save()

            feed = NewsFeed.objects.get_or_create(
                source=source
                title = item['title'],
                summary ="",
                url = item['link'],
            )
            feed.save()


# list3 = [academic_calendar.run(), menu.run(), weather.run()]
# print(list3)
