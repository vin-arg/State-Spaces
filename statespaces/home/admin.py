from django.contrib import admin
from .models import (Building, Amenity, Venue, VenueAmenity, Agent, Customer, Reservation)


class BuildingAdmin(admin.ModelAdmin):
    list_display = ('building_id', 'name', 'address', 'city')
    search_fields = ('name', 'city')


class AmenityAdmin(admin.ModelAdmin):
    list_display = ('amenity_id', 'type', 'description')
    search_fields = ('type',)


class VenueAmenityInline(admin.TabularInline):
    model = VenueAmenity
    extra = 1


class VenueAdmin(admin.ModelAdmin):
    list_display = ('venue_id', 'name', 'venue_type', 'building', 'floor', 'capacity', 'under_renovation')
    search_fields = ('name', 'venue_id')
    list_filter = ('venue_type', 'building', 'under_renovation')
    inlines = [VenueAmenityInline]


class AgentAdmin(admin.ModelAdmin):
    list_display = ('agent_id', 'name')
    search_fields = ('name',)
    list_filter = ('agent_id',)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'birth_date')
    search_fields = ('customer_name',)


class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'reservation_id',
        'number_of_participants',
        'start_datetime',
        'end_datetime',
    )
    list_filter = ('start_datetime',)


admin.site.register(Building, BuildingAdmin)
admin.site.register(Amenity, AmenityAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Reservation, ReservationAdmin)
# Register your models here.
