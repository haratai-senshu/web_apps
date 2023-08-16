"""pj_x URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from django.conf.urls.static import static
from django.views.static import serve  #追加
from django.urls import re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("file_format_converter/", include("text_edit.urls")),
    path("University_Naniritsu_Judge_Kun/", include("univ_app.urls")),
    re_path(r'^media/(?P<path>.*)$', serve, kwargs={'document_root': settings.MEDIA_ROOT})

] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
