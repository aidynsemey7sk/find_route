from django.shortcuts import render

from cities.models import City


__all__=(
    'home',
    )

def home(request):
    cities = City.objects.all()
    context = {'objects_list': cities}
    return render(request, 'cities/home.html', context)
