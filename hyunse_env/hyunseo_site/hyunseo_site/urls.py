"""hyunseo_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from memo.views import memo_view

from profiles.views import home
from profiles.views import taskcheck

from datavisual.views import dv

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^memo/$', memo_view, name='memo'),
    #url(r'^info/$', datavisual_view, name='datavisual_view'),
    #url(r'^memo/', include('memo.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^check/$', taskcheck, name='taskcheck'),
    #url(r'^profiles/', include('profiles.urls')),

    url(r'^dv/$', dv, name='dv'),
]
