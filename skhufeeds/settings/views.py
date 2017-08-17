from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from crawlers.models import Source
from .models import Subscribed
# Create your views here.

## authenticate user with useruid and jwt token
def authUser(request, useruid, token):
    #
    try:
        user = authenticate(useruid=useruid, token=token)
    except User.DoesNotExist:
        return HttpResponseNotFound("존재하지 않는 사용자 입니다.")
    except jwt.InvalidAudienceError:
        return HttpResponseForbidden("만료된 URL 입니다.")
    else:
        login(request, user)
        return HttpResponseRedirect("/settings") # Redirect user to index page of settings app

# Settings index page
@login_required
def index(request):
    user = request.user
    allSources = Source.objects.all()
    subscribedSources = Subscribed.objects.filter(user=user)
    subscribedList = list()
    for item in subscribedSources:
        subscribedList.append(item.source)

    data = { 'all': allSources, 'subscribed': subscribedList }
    return render(request, 'index.html', data)

# Update Subscribtion Settings
@login_required
def updateItem(request):
    return HttpResponse("아직 구현되지 않음.")
