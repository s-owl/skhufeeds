from django.http import JsonResponse
from . import util

cmd = '날씨'

def run():
    util.updateLastCommand(command,user.profile)
    return JsonResponse({
        'message' : {
            'text':  "언제의 날씨를 알고 싶으신가요?"
        },
        'keyboard': {
            'type' : 'buttons',
            'buttons' : ['현재 날씨', '내일 날씨']
        }
    })
