
from django.urls import re_path
from Models import views

urlpatterns = [
    re_path('^api/user/?$', views.UserInfoList.as_view()),
    re_path('^api/user/(?P<id>[a-zA-Z0-9_-]+)/?$', views.UserInfoOne.as_view()),
]
