from .. import getnews
import json, datetime
from . import util
from django.http import JsonResponse

cmd = "학교소식"

def run(user, command, user_key):
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
