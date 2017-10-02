from . import util
from django.http import JsonResponse

cmd = "학식"

def run(user,command,user_key):
    util.updateLastCommand(command,user.profile)
    return JsonResponse({
        'message' : {
            'text': today_date + '\n중식: 없음\n석식: 없음'
        },
        'keyboard': {
            'type' : 'buttons',
            'buttons' : util.defaultBtns
            }
        })
