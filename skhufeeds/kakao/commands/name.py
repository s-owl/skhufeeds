from django.http import JsonResponse
from . import util

cmd = '성명'

def run():
    util.updateLastCommand(command,user.profile)
    return JsonResponse({
        'message':{
            'text': '교수명을 입력하세요.'
        },
        'keyboard' :{
            'type' : 'text'
        }
    })
