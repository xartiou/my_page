from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('type/', views.type),
    path('type/<str:signs_type>/', views.get_info_signs_type, name='list_signs_type'),
    path('<int:sign_zodiac>/', views.get_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_about_sign_zodiac, name='horoskope_name'),
]