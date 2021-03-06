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
from django.conf import settings
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    re_path('^$', RedirectView.as_view(url='index.html')),
    re_path('^api/admin/?', admin.site.urls),
    re_path('^api/api-auth/?', include('rest_framework.urls', namespace='rest_framework')),
    re_path('^api/docs/?', include_docs_urls(title='Document')),
    path('', include('Views.urls')),
    path('', include('Models.urls'))
]

if settings.DEBUG:
    urlpatterns.append(re_path('^(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_VUE}))
else:
    urlpatterns.append(re_path('^(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}))
