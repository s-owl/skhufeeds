from django.conf.urls import url
from . import views,command
# Kakao API 처리
urlpatterns = [
    url(r'^$', views.index),
    url(r'^keyboard/$', views.keyboard),
    url(r'^message$', command.answer),
    url(r'^friend$', views.add_friend),
    url(r'^friend/(?P<user_key>\w+)$', views.del_friend)
]
