from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import json, datetime
from skhufeeds import account
from . import command
from django.contrib.auth.models import User
from settings.models import Profile
from crawlers.models import Phone

default = ['학교소식','연락처','학사일정','날씨','학식','설정']

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    today_date = datetime.date.today().strftime("%m월 %d일")
    command = received_json_data['content']
    user_key = received_json_data['user_key']

    try:
        user = User.objects.get(username = user_key)
        userinfo = Profile.objects.get(user = user)
    except User.DoesNotExist:
        updateLastCommand(command, userinfo)
        return JsonResponse({
            'message' : {
                'text': '친구추가 후 정상적으로 이용하실 수 있습니다.'
                },
            'keyboard': {
                'type' : 'buttons',
                'buttons' : default
                }
            })

    if(userinfo.last_command == '성명'):
        result = Phone.objects.filter(name = command)
        msg = ""
        for item in result:
            msg += '{}:\n   내선번호: {}\n  e-mail: {}\n'.format(Phone.name,Phone.phone,Phone.email)
        if(len(result)==0):
            updateLastCommand(command, userinfo)
            return JsonResponse({
                'message' : {
                    'text': '해당 교수명이 존재하지 않습니다.'
                },
                'keyboard': {
                    'type' : 'buttons',
                    'buttons' : default
                }
            })
        else:
            updateLastCommand(command, userinfo)
            return JsonResponse({
                'message':{
                    'text': msg
                },
                'keyboard':{
                    'type' : 'buttons',
                    'buttons' : default
                }
            })

    elif(userinfo.last_command == '소속'):
        result2 = Phone.objects.filter(desc__contains = command)
        msg2 = ""
        for item2 in result2:
            msg2 += '{}:\n   내선번호: {}\n  e-mail: {}\n'.format(Phone.name,Phone.phone,Phone.email)
        if(len(result2)==0):
            updateLastCommand(command, userinfo)
            return JsonResponse({
                'message' : {
                    'text': '해당 학과명 또는 부서명이 존재하지 않습니다.'
                },
                'keyboard': {
                    'type' : 'buttons',
                    'buttons' : default
                }
            })
        else:
            updateLastCommand(command, userinfo)
            return JsonResponse({
                'message':{
                    'text': msg2
                },
                'keyboard':{
                    'type' : 'buttons',
                    'buttons' : default
                }
            })

    elif(command == '학식'):
        updateLastCommand(command, userinfo)
        return JsonResponse({
            'message' : {
                'text': today_date + '\n중식: 없음\n석식: 없음'
            },
            'keyboard': {
                'type' : 'buttons',
                'buttons' : default
                }
            })
    elif(command == '학교소식'):
        updateLastCommand(command, userinfo)
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
        updateLastCommand(command, userinfo)
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
        updateLastCommand(command, userinfo)
        return JsonResponse({
            'message' : {
                'text': '무엇으로 검색하시겠습니까?\n연락처는 내선번호와 이메일이 제공됩니다.'
            },
            'keyboard': {
                'type' : 'buttons',
                'buttons' : ['성명','소속']
            }
        })
    elif(command == '설정'):
        loginUrl = 'http://ec2-13-124-197-141.ap-northeast-2.compute.amazonaws.com/settings/login/{}/{}'
        tokenUrl = loginUrl.format(user_key,account.getToken(user_key))
        updateLastCommand(command, userinfo)
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
    elif(command == '성명'):
        updateLastCommand(command, userinfo)
        return JsonResponse({
            'message':{
                'text': '교수명을 입력하세요.'
            },
            'keyboard' :{
                'type' : 'text'
            }
        })
    elif(command == '소속'):
        updateLastCommand(command, userinfo)
        return JsonResponse({
            'message':{
                'text': '학과명 또는 부서명을 입력하세요.'
            },
            'keyboard' :{
                'type' : 'text'
            }
        })
    else:
        return HttpResponseNotFound

def updateLastCommand(command, userInfo):
    userInfo.last_command = command
    userInfo.save()
