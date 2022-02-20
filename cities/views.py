from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView, CreateView, UpdateView, DeleteView, ListView
    )
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.contrib import messages

from cities.forms import CityForm
from cities.models import City


__all__=(
    'home', 'CityDetailView', 'CityCreateView', 'CityUpdateView',
    'CityDeleteView', 'CityListView'
    )

def home(request, pk=None):
    '''Отображение с помощью функции'''
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
    lst = Paginator(cities, 3)
    page_number = request.GET.get('page')
    print(page_number)
    page_obj = lst.get_page(page_number)
    print(page_obj)
    context = {'page_obj': page_obj, 'form': form}
    return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'


class CityCreateView(SuccessMessageMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'Город успешно создан'


class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'Город успешно отредактирован'


class CityDeleteView(DeleteView):
    model = City
    # template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')
    
    def get(self, request, *args, **kwargs) :
        messages.success(request, 'Город успешно удален.')
        return self.post(request, *args, **kwargs)


class CityListView(ListView):
    paginate_by = 3
    model = City
    template_name = 'cities/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CityForm()
        context['form'] = form
        return context




