from django.shortcuts import render, redirect
from pages.models import *
from .forms import ReservationForm


def home(request):
    scrolls = MainScrollModel.objects.all().order_by("-pk")
    menu = Menu.objects.all().order_by("-pk")
    context = {
        'scrolls' : scrolls,
        'menu' : menu
    }
    return render(request, 'index.html', context=context)



def reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')
    

