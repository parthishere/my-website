from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from .views import home_view, download_pdf, another_home, change_theme, change_another, cmd_home

app_name = 'portfolio'

urlpatterns = [

    path('h', home_view, name='home'),
    path('', another_home, name='a-home'),
    path('c', cmd_home, name='c-home'),
    path('download-pdf', download_pdf, name='pdf'),
    path('change/', change_theme, name='change-theme'),
    path('change-another/', change_another, name='change-another'),
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('images/favicon.ico'))),
]
