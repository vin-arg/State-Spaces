from django.db import models
from django.contrib.auth.models import User


# Utility function to generate incremental IDs
def generate_auto_id(model, prefix, digits=3):
    last = model.objects.order_by("-" + model._meta.pk.name).first()
    if last:
        last_num = last.pk.replace(prefix, "")
        next_num = int(last_num) + 1 if last_num.isdigit() else 1
    else:
        next_num = 1
    return f"{prefix}{next_num:0{digits}d}"


class Home(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Building(models.Model):
    building_id = models.CharField(max_length=20, primary_key=True, editable=False)
    building_name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.building_id:
            self.building_id = generate_auto_id(Building, "BLD")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.building_name


class Amenity(models.Model):
    amenity_id = models.CharField(max_length=20, primary_key=True, editable=False)
    type = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.amenity_id:
            self.amenity_id = generate_auto_id(Amenity, "AME")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.type


class Venue(models.Model):
    venue_id = models.CharField(max_length=20, primary_key=True, editable=False)
    venue_name = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()
    type = models.CharField(max_length=100)
    floor_area = models.PositiveIntegerField()
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE, to_field="building_id")
    floor = models.CharField(max_length=20)
    under_renovation = models.BooleanField(default=False)
    agent_id = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True, blank=True, to_field="agent_id")
    
    

    def save(self, *args, **kwargs):
        if not self.venue_id:
            self.venue_id = generate_auto_id(Venue, "VEN")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.venue_name


class VenueAmenity(models.Model):
    venue_id = models.ForeignKey(Venue, on_delete=models.CASCADE, to_field="venue_id")
    amenity_id = models.ForeignKey(Amenity, on_delete=models.CASCADE, to_field="amenity_id")
    count = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('venue_id', 'amenity_id')  # prevents duplicates

    def __str__(self):
        return f"{self.venue_id.venue_name} — {self.amenity_id.type} (x{self.count})"

class Agent(models.Model):
    agent_id = models.CharField(max_length=20, primary_key=True, editable=False)
    agent_name = models.CharField(max_length=200)
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE,  null=True, blank=True, to_field="building_id")
    #vanue needed to call the other values but not part of normalized so im not sure
    venue_id = models.ForeignKey(Venue, on_delete=models.CASCADE, null=True, blank=True, to_field="venue_id")


    def save(self, *args, **kwargs):
        if not self.agent_id:
            self.agent_id = generate_auto_id(Agent, "AGT")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.agent_name


class Customer(models.Model):
    customer_id = models.CharField(max_length=20, primary_key=True, editable=False)
    customer_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    location = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if not self.customer_id:
            self.customer_id = generate_auto_id(Customer, "CUS")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.customer_name


class Reservation(models.Model):
    reservation_id = models.CharField(max_length=20, primary_key=True, editable=False)
    venue_id = models.ForeignKey(Venue, on_delete=models.CASCADE, to_field="venue_id")
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, to_field="customer_id")
    participants_qty = models.PositiveIntegerField()
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.reservation_id:
            self.reservation_id = generate_auto_id(Reservation, "RES")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.reservation_id
    

class Renovation(models.Model):
    renovation_id = models.CharField(max_length=20, primary_key=True, editable=False)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    venue_id = models.ForeignKey(Venue, on_delete=models.CASCADE, to_field="venue_id")

    def save(self, *args, **kwargs):
        if not self.renovation_id:
            self.renovation_id = generate_auto_id(Renovation, "REN")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.renovation_id} — {self.venue_id.venue_name}"
    

class Team(models.Model):
    agent_id = models.ForeignKey(Agent, on_delete=models.CASCADE, to_field="agent_id")
    team_name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)

    class Meta:
        unique_together = ("agent_id", "team_name")  # composite key behavior

    def __str__(self):
        return f"{self.team_name} — {self.agent_id.agent_name}"
