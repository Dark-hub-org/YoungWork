import os
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.views.generic.base import RedirectView
from django.views.static import serve
from django.conf.urls.static import static

favicon_view = RedirectView.as_view(url=os.path.join(settings.STATIC_URL, 'favicon.svg'), permanent=True)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('favicon.svg', favicon_view),
                  path('', TemplateView.as_view(template_name='index.html')),
                  path('api/', include('djoser.urls')),
                  path('api/', include('djoser.urls.jwt')),
                  path('api/', include('accounts.urls')),
                  path('', include('profiles.urls')),
                  path('', include('jobs.urls')),
                  path('', include('resume.urls')),
                  path('api/chat/', include('chat.urls')),
                  path('', include('notification.urls')),
                  re_path(r'^media/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.VUE_ROOT, 'media')}),
                  re_path(r'^img/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.VUE_ROOT, 'img')}),
                  re_path(r'^js/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.VUE_ROOT, 'js')}),
                  re_path(r'^css/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.VUE_ROOT, 'css')}),
                  re_path(r'^fonts/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.VUE_ROOT, 'fonts')}),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
