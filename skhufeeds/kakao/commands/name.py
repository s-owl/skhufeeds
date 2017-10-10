from . import util
from django.http import JsonResponse

def run(user, command, user_key):
    util.updateLastCommand(command,user.profile)
    return JsonResponse({
        'message':{
            'text': '교수명을 입력하세요.'
        },
        'keyboard' :{
            'type' : 'text'
        }
    })
