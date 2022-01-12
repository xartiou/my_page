from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def rectangle_area(request, width:int, height:int):
    rectangle_area = width * height
    return HttpResponse(f'Площадь прямоугольника размером {width}х{height} равна {rectangle_area}')

def get_rectangle_area(request, width:int, height:int):
    redirect_url = reverse(rectangle_area, args=[width, height])
    return HttpResponseRedirect(redirect_url)


def square_area(request, width:int):
    square_area = width ** 2
    return HttpResponse(f'Площадь квадрата размером {width} равна {square_area}')

def get_square_area(request, width:int):
    redirect_url = reverse(square_area, args=[width])
    return HttpResponseRedirect(redirect_url)

def circle_area(request, radius:int):
    circle_area = 3.14 * radius ** 2
    return HttpResponse(f'Площадь круга с радиусом {radius} равна {circle_area}')

def get_circle_area(request, radius:int):
    redirect_url = reverse(circle_area, args=[radius])
    return HttpResponseRedirect(redirect_url)

