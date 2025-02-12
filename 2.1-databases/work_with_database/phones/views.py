from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):

    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort')

    match sort:
        case 'name':
            res_sort = phones.order_by('name')
        case 'min_price':
            res_sort = phones.order_by('price')
        case 'max_price':
            res_sort = phones.order_by('price').reverse()
        case _:
            res_sort = phones

    context = {'phones': res_sort,}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug = slug)
    context = {'phone': phone,}
    return render(request, template, context)
