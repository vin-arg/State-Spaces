from django.db import models
from django.contrib.auth.models import User


class Home(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class Building(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Amenity(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class VenueAmenity(models.Model):
    venue = models.ForeignKey("Venue", on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Venue(models.Model):
    venue_id = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    venue_type = models.CharField(max_length=100)  # Meeting room, Pantry, etc.
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor = models.CharField(max_length=20)
    capacity = models.PositiveIntegerField()
    floor_area = models.PositiveIntegerField()
    under_renovation = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField(max_length=200)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Customer(models.Model):
    full_name = models.CharField(max_length=200)
    birth_date = models.DateField()

    def __str__(self):
        return self.full_name
    

class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    number_of_participants = models.PositiveIntegerField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.customer} - {self.venue}"
# Create your models here.
