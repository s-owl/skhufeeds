from crawlers.models import NewsFeed,Source
from settings.models import Subscribed
from django.contrib.auth.models import User


# 구독 5개까지 커머, 6개 이상부터 구독별 피드 갯수 조절 필요
def query_news(user):
    newsfeeds = ""
    sub_list = Subscribed.objects.filter(user=user)
    last_pull = user.profile.last_pull
    for sub in sub_list:
        feeds = NewsFeed.objects.filter(source=sub.source, time__gte=last_pull)
        if(len(feeds)==0):
            feeds = NewsFeed.objects.filter(source=sub.source).order_by('-time')[:3]
        for feed in feeds:
            newsfeeds = newsfeeds + "\n[{}]\n{}\n{}\n".format(sub.source.name, feed.title, feed.url)

    return newsfeeds
