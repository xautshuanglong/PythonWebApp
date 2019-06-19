
from django.urls import re_path
from Models import views

urlpatterns = [
    re_path('^user/?$', views.UserInfoList.as_view()),
    re_path('^user/(?P<id>[a-zA-Z0-9_-]+)/?$', views.UserInfoOne.as_view()),
]
