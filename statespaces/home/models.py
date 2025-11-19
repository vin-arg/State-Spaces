from django.db import models
from django.contrib.auth.models import User


class Home(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class Building(models.Model):
    building_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Amenity(models.Model):
    amenity_id = models.CharField(max_length=20)
    type = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.type

class VenueAmenity(models.Model):
    venue = models.ForeignKey("Venue", on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Venue(models.Model):
    venue_id = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()
    venue_type = models.CharField(max_length=100)  # Meeting room, Pantry, etc.
    floor_area = models.PositiveIntegerField()
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor = models.CharField(max_length=20)
    under_renovation = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Agent(models.Model):
    agent_id = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name

class Customer(models.Model):
    customer_id = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.customer_name
    

class Reservation(models.Model):
    reservation_id = models.CharField(max_length=20)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    number_of_participants = models.PositiveIntegerField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()


# Create your models here.
