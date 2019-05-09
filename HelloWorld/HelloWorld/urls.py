"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.urlpatterns import format_suffix_patterns

from Views import index, hello
from Models import views

urlpatterns = [
    re_path('^$', index.index, name='index'),
    re_path('^index/', index.index, name='index'),
    re_path('^admin/', admin.site.urls),
    re_path('api/', include('rest_framework.urls', namespace='rest_framework')),
    re_path('docs/', include_docs_urls(title='Document')),
    re_path('^hello/$', hello.hello),
    re_path('^user/$', views.UserInfoList.as_view()),
    re_path('^user/(?P<id>[a-zA-Z0-9_-]+)/$', views.UserInfoOne.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
