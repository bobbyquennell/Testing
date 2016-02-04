"""Testing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^artical/(\d{4})/(\d{2})/(\d+)/$',views.artical),
    url(r'^artical/(?P<year>\d{4})/$',views.artical,{'month':11}),
    url(r'^add/(?P<name>\w+)/$',views.add),
    url(r'^delete/(?P<id>\d+)/$',views.delete),
    url(r'^update/(?P<id>\d+)/(?P<name>\w+)/$',views.update),
    url(r'^view/(?P<name>\w+)/$',views.view),
    url(r'^login/$',views.login),
    url(r'^index/$',views.index),
    url(r'^host/$',views.host),
]
