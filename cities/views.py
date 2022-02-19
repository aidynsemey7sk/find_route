from django.shortcuts import get_object_or_404, render

from cities.models import City


__all__=(
    'home',
    )

def home(request, pk=None):
    if pk:
        city = get_object_or_404(City, id=pk)
        context = {'objects_list': city}
        return render(request, 'cities/detail.html', context)
    cities = City.objects.raw("SELECT * FROM cities_city")
    context = {'objects_list': cities}
    return render(request, 'cities/home.html', context)
