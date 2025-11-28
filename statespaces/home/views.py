from django.shortcuts import render
from .models import Home, Venue, Agent, Reservation, Building, VenueAmenity

def home(request):
    home = Home.objects.all()
    return render(request, 'home.html', {'home': home})


def venue_list(request):
    selected_building = request.GET.get("building")

    # Prefetch amenities with quantities
    venues = (Venue.objects.select_related("building").prefetch_related("venueamenity_set__amenity"))

    buildings = Building.objects.all()

    if selected_building:
        venues = venues.filter(building_id=selected_building)

    context = {"venues": venues, "buildings": buildings, "selected_building": selected_building,}

    return render(request, "venue_list.html", context)


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
