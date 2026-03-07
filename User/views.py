from django.shortcuts import render, redirect
from .models import Lenovo

def home_page(request):
    data = Lenovo.objects.all()
    context = {}
    context['datas'] = data
    if request.method == 'POST':
        product = Lenovo.objects.create(
            title = request.POST['title'],
            series_number = request.POST['series_number'],
        )
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def booking(request):
    return render(request, 'booking.html')

def contact(request):
    return render(request, 'contact.html')