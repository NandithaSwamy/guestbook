from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from guestbook import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'guestbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^guestbook/', include('guestbook_app.urls')),
    url(r'^home/(?P<path>.*)$', serve, {'document_root': settings.UI_ROOT, }),
]
