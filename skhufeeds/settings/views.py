from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound, HttpResponseForbidden
from .models import UserInfo
import jwt

# Create your views here.

## authenticate user with useruid and jwt token
def authUser(request, useruid, token):
    #
    try:
        user = authenticate(useruid=useruid, token=token)
    except User.DoesNotExist:
        return HttpResponseNotFound("존재하지 않는 사용자 입니다.")
    except jwt.ExpiredSignatureError:
        return HttpResponseForbidden("만료된 URL 입니다.")
    except jwt.exceptions.InvalidAudienceError:
        return HttpResponseForbidden("사용자 불일치 오류.")
    except jwt.exceptions.DecodeError:
        return HttpResponseForbidden("복호화 오류.")
    else:
        login(request, user)
        return HttpResponse("로그인 성공")
