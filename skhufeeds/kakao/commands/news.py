from django.http import JsonResponse
from . import util
from .. import getnews
import datetime
from django.contrib.auth.models import User

def run():
    newsfeeds = getnews.query_news(user)
    if(len(newsfeeds)<=5):
        newsfeeds = "구독하신 항목이 없습니다.\n설정버튼을 눌러 하나 이상 구독해주세요.\n(설정-설정페이지-구독)"
    user.profile.last_pull = datetime.datetime.utcnow()
    user.save()
    util.updateLastCommand(command,user.profile)
    return JsonResponse({

        'message' : {
            'text': "[{} 학교소식]\n".format(today_date) + newsfeeds
        },
        'keyboard': {
            'type' : 'buttons',
            'buttons' : util.defaultBtns
        }
    })
