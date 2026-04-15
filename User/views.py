from django.shortcuts import render, redirect # type: ignore
from User import models

def index(request):
    banner = models.Banner.objects.last()
    about = models.About.objects.last()
    services = models.Service.objects.all().order_by('-id')[0:4]
    menu_type = models.FoodTypes.objects.all()
    food_dic = {}

    for types in menu_type:
        food = types.foods.all()
        food_dic[types.title] = food

    requested_menu = None
    menu_food = request.GET.get('type')
    if menu_food:
        print(menu_food, "menu food ")
        requested_menu = food_dic.get(menu_food)

    if request.method == 'POST':
        reservation = models.Reservation.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            date = request.POST['date'],
            pax = request.POST['pax'], 
            special_request = request.POST['special_request']
        )
        print(reservation)
        return redirect("index")

    try:
        context = {}
        context['banner'] = banner
        context['about'] = about
        context['about_images'] = about.images.all()[:4]
        context['services'] = services
        context['requested_menu'] = requested_menu
        context['menu_type'] = menu_type
    except Exception as e:
        print(e)  # or handle error properly
    else:
        print("No errors occurred")
    
        
    return render(request, 'index.html', context)




































def about(request):
    return render(request, 'about.html')

def booking(request):
    return render(request, 'booking.html')

def contact(request):
    return render(request, 'contact.html')

def menu(request):
    return render(request, 'menu.html')

def service(request):
    return render(request, 'service.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')