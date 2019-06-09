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
from django.urls import re_path, path, include
from django.views.generic.base import RedirectView
from django.views import static
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    re_path('^$', RedirectView.as_view(url='static/index.html')),
    re_path('^index.html$', RedirectView.as_view(url='static/index.html')),
    re_path('^favicon.ico$', RedirectView.as_view(url='static/favicon.ico')),
    re_path('^admin/', admin.site.urls),
    re_path('^api/', include('rest_framework.urls', namespace='rest_framework')),
    re_path('^docs/', include_docs_urls(title='Document')),
    re_path('^static/(?P<path>.*)$', static.serve,
            {'document_root': 'static'}, name='static'),
    path('', include('Views.urls')),
    path('', include('Models.urls')),
]
