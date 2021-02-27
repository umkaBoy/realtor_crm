from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from django.conf.urls.static import static
from project import settings
from crm.views import base, rest
from crm.views import auth

urlpatterns = [
    re_path('logout', auth.LogoutView.as_view(), name='logout'),
    path('rest/profile', login_required(rest.ProfileRest.as_view()) ,name='rest_profile'),
    path('rest/load-data', login_required(rest.LoadDataRest.as_view()) ,name='load_data_rest'),
    path('', login_required(base.BaseView.as_view()), name='base')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
