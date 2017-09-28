from django.http import JsonResponse
from . import util

cmd = '학사일정'

def run():
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
