from django.shortcuts import render
from .models import Home, Venue, Agent, Reservation, Building, VenueAmenity

def home(request):
    home = Home.objects.all()
    return render(request, 'home.html', {'home': home})


# def venue_list(request):
#     selected_building = request.GET.get("building")
#     venues = (Venue.objects.select_related("building").prefetch_related("venueamenity_set__amenity"))
#     buildings = Building.objects.all()

#     if selected_building:
#         venues = venues.filter(building_id=selected_building)

#     context = {"venues": venues, "buildings": buildings, "selected_building": selected_building,}

#     return render(request, "venue_list.html", context)

def venue_list(request):
    selected_building = request.GET.get("building")
    selected_capacity = request.GET.get("capacity")
    selected_type = request.GET.get("venue_type")

    venues = Venue.objects.all()
    buildings = Building.objects.all()

    # Get distinct venue types
    venue_types = Venue.objects.values_list("venue_type", flat=True).distinct()

    # Filter by building
    if selected_building:
        venues = venues.filter(building__building_id=selected_building)

    # Filter by capacity
    if selected_capacity:
        venues = venues.filter(capacity__gte=selected_capacity)

    # Filter by venue type
    if selected_type:
        venues = venues.filter(venue_type=selected_type)

    return render(request, "venue_list.html", {
        "venues": venues,
        "buildings": buildings,
        "venue_types": venue_types,
        "selected_building": selected_building,
        "selected_capacity": selected_capacity,
        "selected_type": selected_type,
    })




def agent_list(request):
    agents = Agent.objects.all()
    return render(request, 'agent_list.html', {'agents': agents})


def book_reservation(request):
    if request.method == "POST":
        # handle form submission
        pass

    venues = Venue.objects.filter(under_renovation=False)
    agents = Agent.objects.all()
    return render(request, 'book_reservation.html', {'venues': venues, 'agents': agents})


def reservation_list(request):
    reservations = Reservation.objects.select_related("venue", "customer", "agent")
    return render(request, 'reservation_list.html', {'reservations': reservations})
