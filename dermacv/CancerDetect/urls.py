from django.conf.urls import patterns, include, url
from django.conf import settings
from CancerDetect import views
from django.conf.urls.static import static


urlpatterns = patterns('',
        url(r'^$', views.upload, name='upload'),
        url(r'^result/$', views.result, name='result'),
        ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)