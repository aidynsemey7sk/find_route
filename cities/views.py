from django.shortcuts import get_object_or_404, render

from cities.forms import HtmlForm, CityForm
from cities.models import City


__all__=(
    'home',
    )

def home(request, pk=None):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    if pk:
        city = get_object_or_404(City, id=pk)
        context = {'objects_list': city}
        return render(request, 'cities/detail.html', context)
    form = CityForm()
    cities = City.objects.raw("SELECT * FROM cities_city")
    context = {'objects_list': cities, 'form': form}
    return render(request, 'cities/home.html', context)
