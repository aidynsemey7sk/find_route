from django.urls import path

from travel.views import *


urlpatterns = [
    path('', home, name='home'),
]