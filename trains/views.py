from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.contrib import messages
from django.views.generic import (
    DetailView, CreateView, UpdateView, DeleteView, ListView
    )
from django.contrib.auth.mixins import LoginRequiredMixin

from trains.forms import TrainForm
from trains.models import Train


__all__=(
    'home', 'TrainListView', 'TrainDetailView', 
    'TrainCreateView', 'TrainUpdateView', 'TrainDeleteView', 
    )


def home(request, pk=None):
    '''Отображение с помощью функции'''
    trains = Train.objects.raw("SELECT * FROM trains_Train")
    lst = Paginator(trains, 3)
    page_number = request.GET.get('page')
    print(page_number)
    page_obj = lst.get_page(page_number)
    print(page_obj)
    context = {'page_obj': page_obj, 'form': form}
    return render(request, 'trains/home.html', context)


class TrainListView(ListView):
    paginate_by = 10
    model = Train
    template_name = 'trains/home.html'
    

class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/detail.html'


class TrainCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:home')
    success_message = 'Поезд успешно создан'


class TrainUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:home')
    success_message = 'Поезд успешно отредактирован'


class TrainDeleteView(LoginRequiredMixin, DeleteView):
    model = Train
    success_url = reverse_lazy('trains:home')
    
    def get(self, request, *args, **kwargs) :
        messages.success(request, 'Поезд успешно удален.')
        return self.post(request, *args, **kwargs)







