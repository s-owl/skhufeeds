from django.http import JsonResponse, HttpResponseNotFound

def process_cmd(command,user_key):
    if(command == '학식'):
        return JsonResponse({
            'message' : {
                'text': today_date + ' 중식 메뉴: 없음'
                },
            'keyboard': {
                'type' : 'buttons',
                'buttons' : default
                }
            })
    elif(command == '학교소식'):
        return JsonResponse({

            'message' : {
                'text': today_date + ' ' + command + ': 없음'
            },
            'keyboard': {
                'type' : 'buttons',
                'buttons' : default
            }
        })
    elif(command == '날씨'):
        return JsonResponse({

            'message' : {
                'text': today_date + ' ' + command + ': 맑음'
            },
            'keyboard': {
                'type' : 'buttons',
                'buttons' : default
            }
        })
    elif(command == '연락처'):
        return JsonResponse({

            'message' : {
                'text': '김희수: 01040582627'
            },
            'keyboard': {
                'type' : 'buttons',
                'buttons' : ['이름','학과명']
            }
        })
    elif(command == '설정'):
        loginUrl = 'http://ec2-13-124-197-141.ap-northeast-2.compute.amazonaws.com/settings/login?token={}'
        tokenUrl = loginUrl.format(account.getToken(user_key))
        return JsonResponse({
            'message' : {
                "text": "아래 버튼을 눌러 설정페이지로 이동하세요.",
                "message_button": {
                    'label': "설정페이지",
                    'url': tokenUrl
                    }
            },
            'keyboard': {
                'type' : 'buttons',
                'buttons' : default
            }
        })
    elif(command == '이름' or '학과명'):
        return JsonResponse({

            'message' : {
                'text': '아직 구현되지 않았습니다.'
            },
            'keyboard': {
                'type' : 'buttons',
                'buttons' : default
            }
        })
    else:
        return HttpResponseNotFound
