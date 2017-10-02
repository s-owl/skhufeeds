from crawlers.crawlers import weather
from . import util
from django.http import JsonResponse

cmd = "날씨"

def run(user, command, user_key):
    util.updateLastCommand(command,user.profile)
    return JsonResponse({

        'message' : {
            'text':  weather.run(1)
        },
        'keyboard': {
            'type' : 'buttons',
            'buttons' : util.defaultBtns
        }
    })
