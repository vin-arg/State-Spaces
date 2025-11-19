from django.urls import path
from .views import home, venue_list, agent_list, book_reservation, reservation_list

urlpatterns = [
    path('home/', home, name="home"),
    path("venue_list/", venue_list, name="venue_list"),
    path("agent_list/", agent_list, name="agent_list"),
    path("book_reservation/", book_reservation, name="book_reservation"),
    path("reservation_list/", reservation_list, name="reservation_list"),
    

]


