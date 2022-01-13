from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

# Create your views here.
day_dict = {
    'monday': 'Понедельник - день тяжелый.',
    'tuesday': 'Вторник - полегчало',
    'wednesday': 'Среда - неделя почти закончилась',
    'thursday': 'Среда - неделя почти закончилась',
    'friday': 'Пятница -развратница.',
    'saturday': 'Суббота -таки Да',
    'sunday': 'Воскресенье - выходной'
}

def get_about_day_week(request, day_week:str):
    # description = day_dict.get(day_week, None)
    # if description:
    #     return HttpResponse(description)
    # else:
    #     return HttpResponseNotFound(f'Нам ещё не известен такой знак - {day_week}.')
    return render(request, 'week_days/greeting.html')

def get_about_day_week_by_number(request, day_week:int):
    days = list(day_dict)
    if day_week > len(days):
        return HttpResponseNotFound(f'Неправильный номер дня недели {day_week}')
    name_day = days[day_week - 1]
    redirect_url = reverse('day_name', args=[name_day])
    return HttpResponseRedirect(redirect_url)


# def get_about_day_week_by_number(request, day_week:int):
#     if 1 <= day_week <= 7:
#         return HttpResponse(f'<font size="10" color="green"><center>Сегодня {day_week} день недели')
#     else:
#         return HttpResponseNotFound(f'<font size="10" color="red"><center>Нет такого дня недели - {day_week}.')

