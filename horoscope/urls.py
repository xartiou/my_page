from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')



urlpatterns = [
    path('', views.index, name='horoscope_index'),
    path('type/', views.type),
    path('type/<str:signs_type>/', views.get_info_signs_type, name='list_signs_type'),
    path('<my_date:sign_zodiac>', views.get_my_date_converters),
    path('<yyyy:sign_zodiac>/', views.get_yyyy_converters),
    path('<int:sign_zodiac>/', views.get_about_sign_zodiac_by_number),
    path('<my_float:sign_zodiac>/', views.get_my_float_converters),
    path('<str:sign_zodiac>/', views.get_about_sign_zodiac, name='horoskope_name'),
]