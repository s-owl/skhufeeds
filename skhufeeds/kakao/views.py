from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, datetime

# Create your views here.
def index(request):
    return JsonResponse({"result":"true"})

def keyboard(request):
    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['학교소식','연락처','날씨','학식','설정']
    })

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    today_date = datetime.date.today().strftime("%m월 %m일")
    command = received_json_data['content']
    if(command == '학식'):
        return JsonResponse({
            'message' : {
                'text': today_date + '의 ' + command + ' 중식 메뉴입니다'
                },
            'keyboard': {
                'type' : 'buttons',
                'buttons' : ['학교소식','연락처','날씨','학식','설정']
                }
            })
    elif(command == '학교소식'):
        return JsonResponse({

            'message' : {
                'text': today_date + ' ' + command + ': 없음'
            },
            'keyboard': {
                'type' : 'buttons',
                'buttons' : ['학교소식','연락처','날씨','학식','설정']
            }
        })
    elif(command == '날씨'):
        return JsonResponse({

            'message' : {
                'text': today_date + ' ' + command + ': 맑음'
            },
            'keyboard': {
                'type' : 'buttons',
                'buttons' : ['학교소식','연락처','날씨','학식','설정']
            }
        })
    elif(command == '연락처'):
        return JsonResponse({

            'message' : {
                'text': '김희수: 01040582627'
            },
            'keyboard': {
                'type' : 'buttons',
                'buttons' : ['학교소식','연락처','날씨','학식','설정']
            }
        })
    elif(command == '설정'):
        return JsonResponse({

            'message' : {
                'text': 'urlurlurlurl'
            },
            'keyboard': {
                'type' : 'buttons',
                'buttons' : ['학교소식','연락처','날씨','학식','설정']
            }
        })
