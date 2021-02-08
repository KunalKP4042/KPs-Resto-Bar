from django.shortcuts import render
from .models import Aboutus,Why_Choose_Us,Chef

# Create your views here.

def aboutus_list(request):
    about = Aboutus.objects.last()
    why_choose_us = Why_Choose_Us.objects.all()
    chef = Chef.objects.all()
    context = {
        'about':about,
        'why_choose_us':why_choose_us,
        'chef':chef,
    }
    return render(request,"aboutus/about.html",context)

