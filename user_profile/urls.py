import os
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.views.generic.base import RedirectView
from django.views.static import serve
from vacancy import views

favicon_view = RedirectView.as_view(url=os.path.join(settings.STATIC_URL, 'favicon.svg'), permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.svg', favicon_view),
    path('', views.Site.index),
    path('vacancys/', views.Site.index),
    path('create/', views.Site.index),
    path('api/v1/vacancys/', views.VacancyListView.as_view()),
    path('api/v1/vacancy/<int:pk>/', views.VacancyDetailView.as_view()),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^dmedia/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.VUE_ROOT, 'media')}),
    re_path(r'^img/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.VUE_ROOT, 'img')}),
    re_path(r'^js/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.VUE_ROOT, 'js')}),
    re_path(r'^css/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.VUE_ROOT, 'css')}),
    re_path(r'^fonts/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.VUE_ROOT, 'fonts')}),
]
