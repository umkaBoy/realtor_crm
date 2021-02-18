from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from project import settings
from crm.views import base

urlpatterns = [
    path('', base.BaseView.as_view(), name='base')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
