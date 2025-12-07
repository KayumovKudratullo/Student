from django.urls import path, include
from User import views

urlpatterns = [
    path("",views.home_page, name='home')
]