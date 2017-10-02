from . import util
from django.http import JsonResponse
from crawlers.crawlers import menu
def run(user,command,user_key):
    util.updateLastCommand(command,user.profile)
    return JsonResponse({
        'message' : {
            'text': today_date + '\nmenu.run()'
        },
        'keyboard': {
            'type' : 'buttons',
            'buttons' : util.defaultBtns
            }
        })
