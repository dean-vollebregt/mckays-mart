from django.contrib import admin

# Register your models here.

from .models import Home, About, Hour, Contact

class HomeAdmin(admin.ModelAdmin):
    list_diplay = ["title", "message"]

    class Meta:
        model = Home

admin.site.register(Home, HomeAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_diplay = ["title", "description"]

    class Meta:
        model = About

admin.site.register(About, AboutAdmin)


class HourAdmin(admin.ModelAdmin):
    list_diplay =  ["weekday", "from_hour", "to_hour"]

    class Meta:
        model = Hour

admin.site.register(Hour, HourAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_diplay =  ["description", "phone", "email"]

    class Meta:
        model = Contact

admin.site.register(Contact, ContactAdmin)
