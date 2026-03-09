from django.urls import path, include
from User import views

urlpatterns = [
    path("",views.index, name='home'),
    path('about', views.about, name='about'),
    path('booking', views.booking, name='booking'),
    path('contact', views.contact, name='contact'),
    path('menu', views.menu, name='menu'),
    path('service', views.service, name='service'),
    path('team', views.team, name='team'),
    path('testimonial', views.testimonial, name='testimonial'),
]