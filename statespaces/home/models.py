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
            self.building_id = generate_auto_id(Building, "BLDG")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.building_name
    
    class Meta:
        managed=False
        db_table='building'


class Amenity(models.Model):
    amenity_id = models.CharField(max_length=20, primary_key=True, editable=False)
    type = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.amenity_id:
            self.amenity_id = generate_auto_id(Amenity, "AMNT")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.type

    class Meta:
        managed = False
        db_table='amenity'


class Venue(models.Model):
    venue_id = models.AutoField(primary_key=True)
    venue_name = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()
    type = models.CharField(max_length=100)
    floor_area = models.PositiveIntegerField()
    building = models.ForeignKey(Building, on_delete=models.CASCADE, to_field="building_id")
    floor = models.CharField(max_length=20)
    under_renovation = models.BooleanField(default=False)
    agent = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True, blank=True, to_field="agent_id")

    def v_id(self):
    # ensure venue_id is treated as a string and zero-padded
        return str(self.venue_id).zfill(7)

    def __str__(self):
        return self.venue_name
    
    class Meta:
        managed=False
        db_table='venue'


class VenueAmenity(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, to_field="venue_id")
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE, to_field="amenity_id")
    count = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('venue_id', 'amenity_id')  # prevents duplicates

    def __str__(self):
        return f"{self.venue_id.venue_name} — {self.amenity_id.type} (x{self.count})"
    class Meta:
        managed=False
        db_table='venueamenity'

class Agent(models.Model):
    agent_id = models.CharField(max_length=20, primary_key=True, editable=False)
    agent_name = models.CharField(max_length=200)
    building = models.ForeignKey(Building, on_delete=models.CASCADE,  null=True, blank=True, to_field="building_id")


    def save(self, *args, **kwargs):
        if not self.agent_id:
            self.agent_id = generate_auto_id(Agent, "AGNT")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.agent_name
    
    class Meta:
        managed=False
        db_table='agent'


class Customer(models.Model):
    customer_id = models.CharField(max_length=20, primary_key=True, editable=False)
    customer_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    location = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if not self.customer_id:
            self.customer_id = generate_auto_id(Customer, "CSTM")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.customer_name
    
    class Meta:
        managed=False
        db_table='customer'


class Reservation(models.Model):
    reservation_id = models.CharField(max_length=20, primary_key=True, editable=False)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, to_field="venue_id")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, to_field="customer_id")
    participants_qty = models.PositiveIntegerField()
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.reservation_id:
            self.reservation_id = generate_auto_id(Reservation, "RSVT")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.reservation_id
    
    class Meta:
        managed=False
        db_table='reservation'
    

class Renovation(models.Model):
    renovation_id = models.CharField(max_length=20, primary_key=True, editable=False)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, to_field="venue_id")

    def save(self, *args, **kwargs):
        if not self.renovation_id:
            self.renovation_id = generate_auto_id(Renovation, "RNVT")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.renovation_id} — {self.venue.venue_name}"
    class Meta:
        managed=False
        db_table='renovation'
    

class Team(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, to_field="agent_id")
    team_name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)

    class Meta:
        unique_together = ("agent_id", "team_name")  # composite key behavior

    def __str__(self):
        return f"{self.team_name} — {self.agent_id.agent_name}"

    class Meta:
        managed=False
        db_table='team'