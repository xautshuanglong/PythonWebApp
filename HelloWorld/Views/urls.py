
from django.urls import re_path
from Views import hello

urlpatterns = [
    re_path('^hello/?$', hello.hello),
]
