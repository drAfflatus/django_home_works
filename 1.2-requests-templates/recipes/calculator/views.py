from lib2to3.fixes.fix_input import context
import datetime
from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'чай': {
        'чай, пакетик': 1,
        'лимон, ломтик': 1,
        'сахар, ч.л': 3,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }



def show_recip(request):
    count_potion = request.GET.get('servings',1)
    aa= request.path[1:-1]
    el_dict = dict(DATA.get(aa))
    change_dict = el_dict

    for key, value in el_dict.items():
        print(type(value))  # Вы
        el_dict[key]=value*int(count_potion)
    context ={'recipe':el_dict}


    return render(request,'calculator/index.html',context)
