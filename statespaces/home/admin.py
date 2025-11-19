from django.contrib import admin
from .models import (Building, Amenity, Venue, VenueAmenity, Agent, Customer, Reservation)


class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city')
    search_fields = ('name', 'city')


class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


class VenueAmenityInline(admin.TabularInline):
    model = VenueAmenity
    extra = 1


class VenueAdmin(admin.ModelAdmin):
    list_display = ('venue_id', 'name', 'venue_type', 'building', 'floor', 'capacity', 'under_renovation')
    search_fields = ('name', 'venue_id')
    list_filter = ('venue_type', 'building', 'under_renovation')
    inlines = [VenueAmenityInline]


class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'building')
    search_fields = ('name',)
    list_filter = ('building',)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date')
    search_fields = ('full_name',)


class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'venue',
        'number_of_participants',
        'start_datetime',
        'end_datetime',
        'agent'
    )
    search_fields = ('customer__full_name',)
    list_filter = ('agent', 'venue', 'start_datetime')


admin.site.register(Building, BuildingAdmin)
admin.site.register(Amenity, AmenityAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Reservation, ReservationAdmin)
# Register your models here.
