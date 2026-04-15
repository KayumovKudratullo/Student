from django.urls import path, include
from User import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",views.index, name='index'),
    path('about', views.about, name='about'),
    path('booking', views.booking, name='booking'),
    path('contact', views.contact, name='contact'),
    path('menu', views.menu, name='menu'),
    path('service', views.service, name='service'),
    path('team', views.team, name='team'),
    path('testimonial', views.testimonial, name='testimonial'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)