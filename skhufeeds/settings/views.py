from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest
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
    if subscribedSources != None and len(subscribedSources) > 0:
        for item in subscribedSources:
            subscribedList.append(item.source)

    data = { 'all': allSources, 'subscribed': subscribedList }
    return render(request, 'index.html', data)

# Update Subscribtion Settings
@login_required
def updateItem(request):
    if request.method == 'POST':
        source = Source.objects.get(source_id=request.POST.get("source_id"))
        user = request.user

        subscribedItem = Subscribed.objects.get(user=user, source=source)
        isSubscribedClient = request.POST.get("is_subscribed")

        if (isSubscribedClient=="true"):
            if(subscribedItem != None):
                # User wants to remove item. remove object from db
                subscribedItem.delete()
            return HttpResponse("<script>alert('구독 해제 되었습니다.')</script>")


        elif (isSubscribedClient=="false"):
            if (subscribedItem == None):
                # User wants to subscribe. Create and save new object
                newSubscription = subscribe()
                newSubscription.user = user
                newSubscription.source = source
                newSubscription.save()
                return HttpResponse("<script>alert('구독 설정 되었습니다.')</script>")
    else:
        return HttpResponseBadRequest()
