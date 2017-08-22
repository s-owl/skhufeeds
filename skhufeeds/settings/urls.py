from django.conf.urls import url
from . import views #.은 현재 폴더(elections)를 의미합니다.

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/(?P<useruid>\w+)/(?P<token>[\w\'\.\-\_]+)$', views.authUser),
    url(r'^toggle_subscription$', views.updateItem)
]
