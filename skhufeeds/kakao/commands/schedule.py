from crawlers.crawlers import academic_calendar
import json, datetime
from . import util
from django.http import JsonResponse


def run(user, command, user_key):
    util.updateLastCommand(command,user.profile)
    return JsonResponse({
        'message':{
            'text': '[{}월 학사일정]\n\n{}'.format(datetime.datetime.now().month, academic_calendar.run())
        },
        'keyboard' :{
            'type' : 'buttons',
            'buttons' : util.defaultBtns
        }
    })
