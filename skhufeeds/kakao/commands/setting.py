
def run():
    loginUrl = settings.BASEURL+'/settings/login/{}/{}'
    tokenUrl = loginUrl.format(user_key,account.getToken(user_key))
    updateLastCommand(command,user.profile)
    return JsonResponse({
        'message' : {
            "text": "본 설정페이지는 3분동안 유지됩니다.",
            "message_button": {
                'label': "설정페이지",
                'url': tokenUrl
                }
        },
        'keyboard': {
            'type' : 'buttons',
            'buttons' : defaultBtns
        }
    })
