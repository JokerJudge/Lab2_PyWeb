from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Bookings)
admin.site.register(Tickets)
admin.site.register(Ticket_flights)
admin.site.register(Boarding_passes)
admin.site.register(Airports)
admin.site.register(Aircrafts)
admin.site.register(Seats)
admin.site.register(Flights)

