from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import json, datetime
from skhufeeds import account
from . import command


default = ['학교소식','연락처','학사일정','날씨','학식','설정']

# Create your views here.
def index(request):
    return JsonResponse({"result":"true"})

def keyboard(request):
    return JsonResponse({
        'type' : 'buttons',
        'buttons' : default
    })

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
