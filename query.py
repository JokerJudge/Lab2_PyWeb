
Flights.objects.all().filter(departure_airport__airport_name='Пулково', arrival_airport__airport_name='Домодедово') # список рейсов между Пулково и Домодедово
Seats.objects.all().filter(aircraft_code__model='Boieng 777') # список мест
Boarding_passes.all().filter(flight_id__flight_no=321) #вывести посадочные талоны на рейс № 321
Tickets.objects.all().filter(ticket_flights__flight_id__flight_no=321) # cписок билетов с именами на рейс № 321