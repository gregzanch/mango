from django.shortcuts import render

def home(request):
    name = "Mango"
    return render(request, "base.html", {"name": name})