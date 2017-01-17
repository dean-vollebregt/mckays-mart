from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Home(models.Model):
    title = models.CharField(max_length=255, help_text='Home page title')
    message = models.TextField(help_text='Home page message', blank=True)

    class Meta:
        verbose_name_plural = "Home"
    
    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=255, help_text='About page title')
    description = models.TextField(help_text='About page description')

    class Meta:
        verbose_name_plural = "About"
    
    def __str__(self):
        return self.title


class Hour(models.Model):

    WEEKDAYS = [
        (1, ("Monday")),
        (2, ("Tuesday")),
        (3, ("Wednesday")),
        (4, ("Thursday")),
        (5, ("Friday")),
        (6, ("Saturday")),
        (7, ("Sunday")),
    ]

    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.CharField(max_length=255)
    to_hour = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Hours"
        ordering = ('weekday', 'from_hour')
        unique_together = ('weekday', 'from_hour', 'to_hour')

    def __str__(self):
        return u'%s: %s - %s' % (self.get_weekday_display(),
                                 self.from_hour, self.to_hour)


class Contact(models.Model):
    title = models.CharField(max_length=100, help_text='Contact page title')
    description = models.TextField(help_text='Contact page description')
    phone = models.CharField(max_length=50, help_text='Please write in the form (08) 8271-2477')
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "Contact"
    
    def __str__(self):
        return self.title