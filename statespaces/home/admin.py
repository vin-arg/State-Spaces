from django.contrib import admin
from .models import (Building, Amenity, Venue, VenueAmenity, Agent, Customer, Reservation, Renovation, Team)


class BuildingAdmin(admin.ModelAdmin):
    list_display = ('building_id', 'building_name', 'address', 'city')
    search_fields = ('building_name', 'city')


class AmenityAdmin(admin.ModelAdmin):
    list_display = ('amenity_id', 'type', 'description')
    search_fields = ('type',)


class VenueAmenityInline(admin.TabularInline):
    model = VenueAmenity
    extra = 1


class VenueAdmin(admin.ModelAdmin):
    list_display = ('venue_id_format', 'venue_name', 'type', 'building_id', 'floor', 'capacity', 'under_renovation')
    search_fields = ('venue_name', 'venue_id')
    list_filter = ('type', 'building_id', 'under_renovation')
    inlines = [VenueAmenityInline]

    def venue_id_format(self, obj):
        return obj.v_id()
    venue_id_format.short_description = "Venue ID"


class AgentAdmin(admin.ModelAdmin):
    list_display = ('agent_id', 'agent_name')
    search_fields = ('agent_name',)
    list_filter = ('agent_id',)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'birth_date')
    search_fields = ('customer_name',)


class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'reservation_id',
        'participants_qty',
        'start_date_time',
        'end_date_time',
    )
    list_filter = ('start_date_time',)

class RenovationAdmin(admin.ModelAdmin):
    list_display = ("renovation_id", "venue_name", "start_date_time", "end_date_time")
    search_fields = ("renovation_id", "venue_id__venue_name")
    list_filter = ("venue_id",)

    def venue_name(self, obj):
        return obj.venue_id.venue_name
    venue_name.short_description = "Venue"

class TeamAdmin(admin.ModelAdmin):
    list_display = ("id", "team_name", "agent_name", "job")
    search_fields = ("team_name", "agent__agent_name", "job")

    def agent_name(self, obj):
        return obj.agent.agent_name
    agent_name.short_description = "Agent"



admin.site.register(Building, BuildingAdmin)
admin.site.register(Amenity, AmenityAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Renovation, RenovationAdmin)
admin.site.register(Team, TeamAdmin)
# Register your models here.
