from django.shortcuts import render
from .models import Category

# Create your views here.

def category_page(request):
    category_page = Category.objects.all().filter(is_available=True)
    contex = {
        'category_page': category_page,
    }   
    return render(request, 'store.html', contex)

