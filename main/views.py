from django.shortcuts import render
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

# Create your views here.
def index(req):
    return render(req, 'index.html')

def filter(req):
    cek = req.GET.get('price')
    cek1 = req.GET.get('order')
    if cek is not None and cek1 is not None:
        query = models.Product.objects.filter(product_price=cek, product_minimum_order=cek1)
        return render(req, 'filter.html',{
            'data': query,
            })

    query = models.Product.objects.all()
    page = req.GET.get('page', 1)
    paginator = Paginator(query, 10)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = Paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return render(req, 'filter.html',{
        'data': data,
        })