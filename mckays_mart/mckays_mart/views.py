from django.shortcuts import render
from photos.models import Living, Dining, Bedroom, Hallway, Office, Musical, Art
from info.models import Home

def home_page(request):

    home_queryset = Home.objects.all()
    living_queryset = Living.objects.filter(featured=True)
    dining_queryset = Dining.objects.filter(featured=True)
    bedroom_queryset = Bedroom.objects.filter(featured=True)
    hallway_queryset = Hallway.objects.filter(featured=True)
    office_queryset = Office.objects.filter(featured=True)
    musical_queryset = Musical.objects.filter(featured=True)
    art_queryset = Art.objects.filter(featured=True)

    featured = {
        "home_queryset": home_queryset,
        "living_queryset": living_queryset,
        "dining_queryset": dining_queryset,
        "bedroom_queryset": bedroom_queryset,
        "hallway_queryset": hallway_queryset,
        "office_queryset": office_queryset,
        "musical_queryset": musical_queryset,
        "art_queryset": art_queryset,
    }
    return render(request, "home.html", featured)