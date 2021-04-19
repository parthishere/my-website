from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from .views import HomeView

app_name='profile'

urlpatterns = [
    
    path('', HomeView.as_view(), name='home'),
    # path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico')))
]
