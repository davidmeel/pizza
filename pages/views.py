from django.shortcuts import render, redirect
from pages.models import *


def home(request):
    scrolls = MainScrollModel.objects.all().order_by("-pk")
    menu = Menu.objects.all().order_by("-pk")
    context = {
        'scrolls' : scrolls,
        'menu' : menu
    }
    return render(request, 'index.html', context=context)