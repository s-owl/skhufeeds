from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import json, datetime
from . import account


default = ['학교소식','연락처','날씨','학식','설정']

# Create your views here.
def index(request):
    return JsonResponse({"result":"true"})

def keyboard(request):
    return JsonResponse({
        'type' : 'buttons',
        'buttons' : default
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
        return JsonResponse({

            'message' : {
                'text': 'urlurlurlurl'
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

@csrf_exempt
def del_friend(request, user_key):
    print("Request path : ",request.path)
    print("Request path info : ",request.path_info)
    if request.method == "DELETE":
        print("Deleting user {}".format(user_key))
        account.deleteUser(user_key)
        return JsonResponse({"result":"done"})
    else:
        return HttpResponseNotFound

# @csrf_exempt
# def del_friend(request, user_key):
#     # json_str = ((request.body).decode('utf-8'))
#     # received_json_data = json.loads(json_str)
#     # user_key = received_json_data['user_key']
@csrf_exempt
def add_friend(request):
    print("Request path : ",request.path)
    print("Request path info : ",request.path_info)
    if request.method == "POST":
        json_str = ((request.body).decode('utf-8'))
        received_json_data = json.loads(json_str)
        user_key = received_json_data['user_key']
        account.registerNewUser(user_key)
        return JsonResponse({"result":"done"})
    else:
        return HttpResponseNotFound

# @csrf_exempt
# def del_friend(request, user_key):
#     if request.method == "POST":
#         json_str = ((request.body).decode('utf-8'))
#         received_json_data = json.loads(json_str)
#         user_key = received_json_data['user_key']
#         account.registerNewUser(user_key)
#         return JsonResponse({"result":"done"})
#
#     elif request.method == "DELETE":
#         print("Deleting user {}".format(user_key))
#         account.deleteUser(user_key)
#         return JsonResponse({"result":"done"})
#
#     else:
#         return HttpResponseNotFound

#
#
#     else:
#         return HttpResponseNotFound
