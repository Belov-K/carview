from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .models import Car

def index(request):
    all_car_list=Car.objects.all()
    return render(request, 'cars/list.html', {'all_car_list': all_car_list})

def detail  (request, car_id):
    try:
        a=Car.objects.get(id=car_id)
    except:
        raise Http404('машина не найдена')

    image_list=a.carimage_set.all()
    print(image_list)
    return render(request, 'cars/detail.html', {'car': a, 'image_list': image_list})