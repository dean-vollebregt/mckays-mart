from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Bathroom(models.Model):
    description = models.CharField(max_length=200)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(
            null=False,
            blank=False, 
            width_field="width", 
            height_field="height",
    )
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    price = models.CharField(max_length=200)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name_plural ="Bathroom"
        ordering =["-timestamp"]

class Bedroom(models.Model):
    description = models.CharField(max_length=200)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(
            null=False,
            blank=False, 
            width_field="width", 
            height_field="height",
    )
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    price = models.CharField(max_length=200)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name_plural ="Bedroom"
        ordering =["-timestamp"]

class Dining(models.Model):
    description = models.CharField(max_length=200)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(
            null=False,
            blank=False, 
            width_field="width", 
            height_field="height",
    )
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    price = models.CharField(max_length=200)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name_plural ="Dining"
        ordering =["-timestamp"]

class Hallway(models.Model):
    description = models.CharField(max_length=200)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(
            null=False,
            blank=False, 
            width_field="width", 
            height_field="height",
    )
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    price = models.CharField(max_length=200)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name_plural ="Hallway"
        ordering =["-timestamp"]

class Living(models.Model):
    description = models.CharField(max_length=200)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(
            null=False,
            blank=False, 
            width_field="width", 
            height_field="height",
    )
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    price = models.CharField(max_length=200)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name_plural ="Living"
        ordering =["-timestamp"]

class Office(models.Model):
    description = models.CharField(max_length=200)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(
            null=False,
            blank=False, 
            width_field="width", 
            height_field="height",
    )
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    price = models.CharField(max_length=200)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name_plural ="Office"
        ordering =["-timestamp"]

class Musical(models.Model):
    description = models.CharField(max_length=200)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(
            null=False,
            blank=False, 
            width_field="width", 
            height_field="height",
    )
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    price = models.CharField(max_length=200)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name_plural ="Musical"
        ordering =["-timestamp"]

class Art(models.Model):
    description = models.CharField(max_length=200)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(
            null=False,
            blank=False, 
            width_field="width", 
            height_field="height",
    )
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    price = models.CharField(max_length=200)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name_plural ="Art"
        ordering =["-timestamp"]



    








