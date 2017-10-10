from . import util
from django.http import JsonResponse
from django.utils import timezone
from crawlers.models import Diet
from datetime import datetime

def run(user,command,user_key):
    util.updateLastCommand(command,user.profile)
    date = timezone.now()

    try:
        # 오늘 날자에 해당하는 식단을 DB 에서 조회
        result = Diet.objects.get(date__year=date.year,
                                  date__month=date.month,
                                  date__day=date.day)
        # 문자열 조립
        menu = "{}년 {}월 {}일 식단!\n[중식A]\n{}\n\n[중식B]\n{}\n\n[석식]\n{}".format(
            result.date.year,
            result.date.month,
            result.date.day+1,
            result.lunchA,
            result.lunchB,
            result.dinner)
    except Diet.DoesNotExist:
        # 없는경우, 안내 표시
        menu = "해당 요일에 학식이 없습니다!"

    # 클라이언트에 응답
    return JsonResponse({
        'message' : {
            'text': menu
        },
        'keyboard': {
            'type' : 'buttons',
            'buttons' : util.defaultBtns
            }
        })
