from django.contrib import admin
from .models import  Bedroom, Dining, Hallway, Living, Office, Musical, Art
# Register your models here.

class BedroomAdmin(admin.ModelAdmin):
    list_diplay = ["description", "timestamp", "price"]

    class Meta:
        model = Bedroom

admin.site.register(Bedroom, BedroomAdmin)


class DiningAdmin(admin.ModelAdmin):
    list_diplay = ["description", "timestamp", "price"]

    class Meta:
        model = Dining

admin.site.register(Dining, DiningAdmin)


class HallwayAdmin(admin.ModelAdmin):
    list_diplay = ["description", "timestamp", "price"]

    class Meta:
        model = Hallway

admin.site.register(Hallway, HallwayAdmin)


class LivingAdmin(admin.ModelAdmin):
    list_diplay = ["description", "timestamp", "price"]

    class Meta:
        model = Living

admin.site.register(Living, LivingAdmin)


class OfficeAdmin(admin.ModelAdmin):
    list_diplay = ["description", "timestamp", "price"]

    class Meta:
        model = Office

admin.site.register(Office, OfficeAdmin)


class MusicalAdmin(admin.ModelAdmin):
    list_diplay = ["description", "timestamp", "price"]

    class Meta:
        model = Musical

admin.site.register(Musical, MusicalAdmin)


class ArtAdmin(admin.ModelAdmin):
    list_diplay = ["description", "timestamp", "price"]

    class Meta:
        model = Art

admin.site.register(Art, ArtAdmin)


