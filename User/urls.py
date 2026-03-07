from django.urls import path, include
from User import views

urlpatterns = [
    path("",views.home_page, name='home'),
    path('about', views.about, name='about'),
    path('booking', views.booking, name='booking'),
    path('contact', views.contact, name='contact'),

]