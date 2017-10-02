from . import util
from django.http import JsonResponse
from django.utils import timezone
from crawlers.models import Diet

def run(user,command,user_key):
    util.updateLastCommand(command,user.profile)
    date = timezone.now()

    result = Diet.objects.get(date__year=date.year, date__month=date.month, date__day=date.day)

    if(result == None):
        menu = "해당 요일에 학식이 없습니다."
    else:
        menu = "{} 메뉴\n중식A: {}\n중식B: {}\n석식: {}".format(result.date,result.lunchA,result.lunchB,result.dinner)

    return JsonResponse({
        'message' : {
            'text': menu
        },
        'keyboard': {
            'type' : 'buttons',
            'buttons' : util.defaultBtns
            }
        })
