from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import models
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    filter = request.GET.get('sort', 'Not')

    template = 'catalog.html'
    if filter == 'Not':
        data_ = Phone.objects.all()
    elif filter == "min_price":
        data_ = Phone.objects.order_by('price')

    elif filter == "max_price":
        data_ = Phone.objects.order_by('-price')
    else:
        data_ = Phone.objects.order_by(filter)



    # print("ВЫВОД")
    # for el in data_:
    #     print(f'{el.name} {el.slug} ')
    context = {'phones': data_}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    print(phone.price)
    context = {'phone': phone}
    return render(request, template, context)


def get_data(request):
    data_ = Phone.objects.all()
    list_phone =[]
    [list_phone.append(str(el)) for el in data_]
    # for phon in data_:
    #     print(phon)
    #     list_phone.append(str(phon))
    return HttpResponse(list_phone)




