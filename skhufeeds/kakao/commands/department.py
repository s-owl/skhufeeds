from django.http import JsonResponse
from . import util

cmd = '소속'

def run():
    util.updateLastCommand(command,user.profile)
    return JsonResponse({
        'message':{
            'text': '학과명 또는 부서명을 입력하세요.'
        },
        'keyboard' :{
            'type' : 'text'
        }
    })
