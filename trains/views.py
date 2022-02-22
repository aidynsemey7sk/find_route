from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView, CreateView, UpdateView, DeleteView, ListView
    )
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.contrib import messages

from trains.forms import TrainForm
from trains.models import Train


__all__=(
    'home', 'TrainListView', 'TrainDetailView',
    #  'TrainCreateView', 'TrainUpdateView',
    # 'TrainDeleteView', 
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
    paginate_by = 3
    model = Train
    template_name = 'trains/home.html'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     form = TrainForm()
    #     context['form'] = form
    #     return context


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/detail.html'


# class TrainCreateView(SuccessMessageMixin, CreateView):
#     model = Train
#     form_class = TrainForm
#     template_name = 'trains/create.html'
#     success_url = reverse_lazy('trains:home')
#     success_message = 'Город успешно создан'


# class TrainUpdateView(SuccessMessageMixin, UpdateView):
#     model = Train
#     form_class = TrainForm
#     template_name = 'trains/update.html'
#     success_url = reverse_lazy('trains:home')
#     success_message = 'Город успешно отредактирован'


# class TrainDeleteView(DeleteView):
#     model = Train
#     # template_name = 'trains/delete.html'
#     success_url = reverse_lazy('trains:home')
    
#     def get(self, request, *args, **kwargs) :
#         messages.success(request, 'Город успешно удален.')
#         return self.post(request, *args, **kwargs)







