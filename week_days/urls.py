from django.urls import path
from . import views

urlpatterns = [
    path('<int:day_week>/', views.get_about_day_week_by_number),
    path('<str:day_week>/', views.get_about_day_week, name='day_name'),
]
