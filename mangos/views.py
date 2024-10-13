from django.shortcuts import render

from mangos.models import Mango, Country


def home(request):
    return render(request, "home.html")

def mangos(request):
    mangos = Mango.objects.all()
    return render(request, "mangos.html", { "mangos": mangos })

def countries(request):
    countries = Country.objects.all()
    return render(request, "countries.html", { "countries": countries })