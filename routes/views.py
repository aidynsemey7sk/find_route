from django.shortcuts import render
from django.contrib import messages

from routes.form import RouteForm
from routes.utils import get_routes

__all__=(
    'home',
    )

def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form':form})


def find_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as ex:
                messages.error(request, ex)
                return render(request, 'routes/home.html', {'form': form})
            return render(request, 'routes/home.html', context)
        return render(request, 'routes/home.html', {'form': form})
    else:
        form = RouteForm()
        messages.error(request, 'Нет данных для поиска')
        return render(request, 'routes/home.html', {'form': form})
