from django.contrib import admin
from django.urls import path, include
from edc_base.views import LoginView, LogoutView
from edc_lab.admin_site import edc_lab_admin

from .views import HomeView, AdministrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', edc_lab_admin.urls),
    path('accounts/login/', LoginView.as_view(), name='login_url'),
    path('login/', LoginView.as_view(), name='login_url'),
    path('logout/', LogoutView.as_view(
        pattern_name='login_url'), name='logout_url'),
    path('admininistration/', AdministrationView.as_view(),
         name='administration_url'),
    path('admininistration/', HomeView.as_view(manual_revision='1.0'),
         name='subject_models_url'),
    path('edc/', include('edc_base.urls')),
    path('edc_device/', include('edc_device.urls')),
    path('edc_protocol/', include('edc_protocol.urls')),
    path('edc_label/', include('edc_label.urls')),
    path('edc_lab/', include('edc_lab.urls')),
    path('lab/', include('edc_lab_dashboard.urls')),
    path('', HomeView.as_view(manual_revision='1.0'), name='home_url'),
]
