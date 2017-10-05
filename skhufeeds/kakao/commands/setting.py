from skhufeeds import account
from django.conf import settings
from . import util
from django.http import JsonResponse

def run(user, command, user_key):
    loginUrl = settings.BASEURL+'/settings/login/{}/{}'
    newToken = account.getToken(user_key)
    tokenUrl = loginUrl.format(user_key, newToken)

    # Store new token for verification
    user.profile.token = newToken
    user.save()

    util.updateLastCommand(command,user.profile)
    return JsonResponse({
        'message' : {
            "text": "아래 설정페이지 버튼을 눌러주세요.\n버튼은 3분동안 활성화됩니다.",
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
