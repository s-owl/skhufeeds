from . import util
from django.http import JsonResponse

def run(user, command, user_key):
    util.updateLastCommand(command,user.profile)
    return JsonResponse({
        'message':{
            'text': '학과명 또는 부서명을 입력해주세요!.'
        },
        'keyboard' :{
            'type' : 'text'
        }
    })
