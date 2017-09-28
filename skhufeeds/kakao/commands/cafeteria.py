from django.http import JsonResponse
from . import util

cmd = '학식'

def run():
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
