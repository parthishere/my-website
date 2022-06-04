from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from .views import home_view, download_pdf

app_name='profile'

urlpatterns = [
    
    path('', home_view, name='home'),
    path('download-pdf', download_pdf, name='pdf'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico')))
]
