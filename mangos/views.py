from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from mangos.models import Mango, Country
from .forms import NewMangoForm

def home(request):
    return render(request, "home.html")

def mangos(request):
    mangos = Mango.objects.all()
    return render(request, "mangos.html", { "mangos": mangos })

def new_mango(request):
    initial = {"name": "New Mango"}
    if request.method == "POST":
        form = NewMangoForm(request.POST, initial=initial)
    else:
        form = NewMangoForm(initial=initial)
    for name, value in request.POST.items():
        print("{}: ({}) {}".format(name, type(value), value))

    if request.method == "POST":
        form = NewMangoForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format(name, type(value), value))

    countries = Country.objects.all()
    return render(request, "new-mango.html", { "countries": countries })

def countries(request):
    countries = Country.objects.all()
    return render(request, "countries.html", { "countries": countries })

def new_country(request):
    return render(request, "new-country.html")
