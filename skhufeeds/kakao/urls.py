from django.conf.urls import url
from . import views #.은 현재 폴더(elections)를 의미합니다.

urlpatterns = [
    url(r'^$', views.index),
    url(r'^keyboard/', views.keyboard),
    url(r'^message', views.answer),
    url(r'^friend/', views.add_friend),
    url(r'^friend/(?P<user_key>)', views.del_friend)
    # url(r'^answer/', views.answer)
    #위의 urls.py와는 달리 include가 없습니다.
    # url(r'^areas/(?P<area>[가-힣]+)/$', views.areas),
    # url(r'^areas/(?P<area>[가-힣]+)/results$', views.results),
    # url(r'^polls/(?P<poll_id>\d+)/$', views.polls), #이 url에 대한 요청을 views.polls가 처리하게 만듭니다.
]
