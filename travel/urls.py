from django.contrib import admin
from django.urls import path, include
from cities.views import *
from routes.views import find_routes, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cities/', include(('cities.urls', 'cities'))),
    path('trains/', include(('trains.urls', 'trains'))),
    path('', home, name='home'),
    path('find_routes/', find_routes, name='find_routes'),
]
