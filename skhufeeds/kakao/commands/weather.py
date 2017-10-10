from crawlers.crawlers import weather
from . import util
from django.http import JsonResponse

def run(user, command, user_key):
    util.updateLastCommand(command,user.profile)
    return JsonResponse({

        'message' : {
            'text':  weather.run(3)
        },
        'keyboard': {
            'type' : 'buttons',
            'buttons' : util.defaultBtns
        }
    })
