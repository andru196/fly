"""fly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.urls import re_path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='home'),
    re_path(r'^login/(?P<log>\d+)', views.login),
    re_path(r'^login', views.login),
    re_path(r'^prof', views.prof),
    re_path(r'^reg/(?P<log>\d+)', views.regist),
    re_path(r'^reg', views.regist),
    re_path(r'^logout', views.log_out),
    path('^upload_pic', views.upload_pic, name="upload_pic"),
    re_path(r'^', views.index),

    path('admin/', admin.site.urls),
]
#if settings.DEBUG:
#    urlpatterns += ('',
#        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#        'document_root': settings.MEDIA_ROOT}))
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
