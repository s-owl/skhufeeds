from .models import Source, NewsFeed, Contact
import datetime
from .crawlers.notice import college, credit, event, lesson, notice, scholarship
from .crawlers.info import info, manage, welfare_student
from .crawlers import academic_calendar, menu, skhu, weather
from background_task import background

@background(schedule=10)
def run_crawler():
    list1 = [info.run(), manage.run(), welfare_student.run()]
    print(list1)
    for group in list1:
        for item in group:
            phone = Contact.objects.create()
            phone.name = item['name']
            phone.desc = item['class'] + item['task'] + item['fax']
            phone.phone = models.CharField['phone']
            phone.save()

    list2 = [college.run(), credit.run(), event.run(), lesson.run(), notice.run(), scholarship.run()]
    print(list2)
    for main in list1:
        for top in main:
            news = NewsFeeds()
            news.time = datetime.datetime.utcnow()
            news.title = top['title']
            news.summary =""
            news.url = top['link']
            news.save()


list3 = [academic_calendar.run(), menu.run(), weather.run()]
print(list3)
