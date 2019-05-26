
from django.urls import re_path
from Views import index, hello

urlpatterns = [
    re_path('^$', index.index, name='index'),
    re_path('^index/', index.index, name='index'),
    re_path('^hello/$', hello.hello),
]
