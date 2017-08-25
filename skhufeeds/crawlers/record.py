from models import Source, NewsFeeds, Contact
import datetime
from crawlers.notice import college, credit, event, lesson, notice, scholarship
from crawlers.info import info, manage, welfare_student
from crawlers import academic_calendar, menu, skhu, weather

list1 = [info.run(), manage.run(), welfare_student.run()]
print(list1)
for group in list1:
    for item in group:
        contact = Contact.objects.create()
        contact.name = item['name']
        contact.desc = item['class'] + item['task'] + item['fax']
        contact.phone = models.CharField['phone']
        contact.save()

# Update NewsFeed Data
list2 = [college.run(), credit.run(), event.run(), lesson.run(), notice.run(), scholarship.run()]
print(list2)
for main in list1:
    src_info = main.['source']
    src = Source.objects.get_or_create(
        name=src_info['name'],
        url=src_info['url'],
        desc=src_info['desc'])
    for top in main['data']:
        news = NewsFeeds.objects.get_or_create(
            source=src,
            time = datetime.datetime.utcnow()
            title = top['title']
            summary =""
            url = top['link'])
        news.save()

S

list3 = [academic_calendar.run(), menu.run(), skhu.run(), weather.run()]
print(list3)
