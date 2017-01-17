from django.shortcuts import render

# Create your views here.

from .models import Living, Dining, Bedroom, Bathroom, Hallway, Office, Musical, Art

def living_list(request):
    queryset = Living.objects.all()
    context = {
        "livings": queryset,
    }
    return render(request, "photos/living.html", context)


def dining_list(request):
    queryset = Dining.objects.all()
    context = {
        "dinings": queryset,
    }
    return render(request, "photos/dining.html", context)


def bedroom_list(request):
    queryset = Bedroom.objects.all()
    context = {
        "bedrooms": queryset,
    }
    return render(request, "photos/bedroom.html", context)


def bathroom_list(request):
    queryset = Bathroom.objects.all()
    context = {
        "bathrooms": queryset,
    }
    return render(request, "photos/bathroom.html", context)


def hallway_list(request):
    queryset = Hallway.objects.all()
    context = {
        "hallways": queryset,
    }
    return render(request, "photos/hallway.html", context)


def office_list(request):
    queryset = Office.objects.all()
    context = {
        "offices": queryset,
    }
    return render(request, "photos/office.html", context)


def musical_list(request):
    queryset = Musical.objects.all()
    context = {
        "musicals": queryset,
    }
    return render(request, "photos/musical.html", context)


def art_list(request):
    queryset = Art.objects.all()
    context = {
        "arts": queryset,
    }
    return render(request, "photos/art.html", context)





