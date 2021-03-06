from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# def leo (request):
#     return HttpResponse('Знак зодиака Лев')

# словарь знаков зодиака
zodiac_dict = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)",
}

# словарь стихий знаков зодиака
element_sign = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'aquarius', 'pisces'],
}

# функция для страницы меню index
def index(request):
    zodiacs = list(zodiac_dict)
    li_sign = ''
    for sign in zodiacs:
        redirect_path = reverse('horoskope_name', args=[sign])
        li_sign += f"<li> <a href='{redirect_path}'> {sign.title()} </a> </li>"
    response = f"""
    <ol>
        {li_sign}
    </ol>
    """
    return HttpResponse(response)


# функция для страницы типов стихий type
def type(request):
    elements = list(element_sign)
    li_elements = ''
    for el in elements:
        redirect_path = reverse('list_signs_type', args=[el])
        li_elements += f"<li><a href='{redirect_path}'>{el.title()}</a> </li>"

    response = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(response)


# функция для динамического url знаков стихий
def get_info_signs_type(request, signs_type: str):
    li_sign_type = ''
    if element_sign.get(signs_type):
        for el in element_sign.get(signs_type):
            redirect_path = reverse('horoskope_name', args=[el])
            li_sign_type += f"<li><a href='{redirect_path}'>{el.title()}</a></li>"
        response = f"""
            <ul>
                {li_sign_type}
            </ul>
            """
        return HttpResponse(response)
    else:
        return HttpResponseNotFound(f'<h2><center>Кто такой? - {signs_type}.</h2>')


# функция для динамического url с запросом str
def get_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(f'<font size="10" color="green"><center>{description}')
    else:
        return HttpResponseNotFound(f'<h2><center>Нам ещё не известен такой знак - {sign_zodiac}.</h2>')


# функция для динамического url с запросом int
def get_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'<h2><center>Неправильный номер знака зодиака {sign_zodiac}</h2>')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoskope_name', args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)
