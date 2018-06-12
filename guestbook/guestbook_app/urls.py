from django.conf.urls import include, url
from django.contrib import admin
from guestbook_app.views import Sampleview

urlpatterns = [
   url(r'^$', Sampleview.as_view()),
   url(r'(?P<row_id>[0-9][0-9]*)$', Sampleview.as_view()),
]

