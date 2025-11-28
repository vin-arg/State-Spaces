from django.shortcuts import render
from .models import Home, Venue, Agent, Reservation, Building, VenueAmenity

def home(request):
    home = Home.objects.all()
    return render(request, 'home.html', {'home': home})


def venue_list(request):
    selected_building = request.GET.get("building")
    selected_capacity = request.GET.get("capacity")
    selected_type = request.GET.get("type")

    venues = Venue.objects.all()
    buildings = Building.objects.all()
    venue_types = Venue.objects.values_list("type", flat=True).distinct()

    
    if selected_building:
        venues = venues.filter(building_id__building_id=selected_building)

    # Filter by capacity
    if selected_capacity:
        venues = venues.filter(capacity__gte=selected_capacity)

    # Filter by type
    if selected_type:
        venues = venues.filter(type=selected_type)

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
    reservations = Reservation.objects.select_related("venue_id", "customer_id")
    return render(request, 'reservation_list.html', {'reservations': reservations})
