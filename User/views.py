from django.shortcuts import render, redirect
from .models import Lenovo

def home_page(request):
    data = Lenovo.objects.all()
    context = {}
    context['datas'] = data
    return render(request, 'index.html', context)
