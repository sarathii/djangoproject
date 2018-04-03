from django.shortcuts import render
from django.http import Http404
from .models import Items






def sh(request):
    ha = Items.objects.all()
    return render (request,'account/product.html',{'ha':ha})

def show(request,items_id):
    try:
        i = Items.objects.get(pk=items_id)
    except Items.DoesNotExist:
        raise Http404("item is not available")

    return render(request, 'account/productview.html', {'i': i})

def home(request):
    return render(request,'account/home.html')






