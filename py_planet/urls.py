# -*- coding: utf8 -*-

from django.conf.urls import url

from .views import CommandReceiveView

urlpatterns = [
    url(r'^bot/(?P<bot_token>.+)/$', CommandReceiveView.as_view(), name='command'),
]
