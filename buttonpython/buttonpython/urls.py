"""buttonpython URL Configuration

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
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.button),
    url(r'^output', views.output, name="script1"),
    url(r'^normal', views.normal, name="normal"),
    url(r'^roombook', views.roombook, name="roombook"),
    url(r'^name', views.name, name="name"),
    url(r'^savename', views.saveName, name="saveName"),
    url(r'^days', views.days, name="days"),
    url(r'^selectroom', views.selectroom, name="selectroom"),
    url(r'^payment', views.payment, name="payment"),
    url(r'^confirm', views.confirm, name="confirm"),
]
