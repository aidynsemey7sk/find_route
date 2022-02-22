from django.shortcuts import render

from routes.form import RouteForm

__all__=(
    'home',
    )

def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form':form})
