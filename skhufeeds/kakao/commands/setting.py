from skhufeeds import account
from django.conf import settings
from . import util
from django.http import JsonResponse

cmd = "설정"

def run(user, command, user_key):
    loginUrl = settings.BASEURL+'/settings/login/{}/{}'
    tokenUrl = loginUrl.format(user_key,account.getToken(user_key))
    util.updateLastCommand(command,user.profile)
    return JsonResponse({
        'message' : {
            "text": "위 설정페이지는 3분동안 유지됩니다.",
            "message_button": {
                'label': "설정페이지",
                'url': tokenUrl
                }
        },
        'keyboard': {
            'type' : 'buttons',
            'buttons' : util.defaultBtns
        }
    })
