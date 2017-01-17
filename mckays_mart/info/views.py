from django.shortcuts import render
from .models import Home, About, Hour, Contact

# Create your views here.


from django.conf import settings


def home(request):
    queryset = Home.objects.all()
    context = {
        "homes": queryset,
    }
    return render(request, context)

def about(request):
    queryset = About.objects.all()
    context = {
        "abouts": queryset,
    }
    return render(request,'info/about.html', context)

def hours(request):
    queryset = Hour.objects.all()
    context = {
        "hours": queryset,
    }

    return render(request,'info/hours.html', context)

def contact(request):

    queryset = Contact.objects.all()
    context = {
        "contacts": queryset,
    }
    return render(request,'info/contact.html', context)

