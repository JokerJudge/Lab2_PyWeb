from django.db import models

# Create your models here.


class Bookings(models.Model):
	book_ref = models.AutoField(primary_key = True)
	book_date = models.DateField(null = False)
	total_amount = models.PositiveIntegerField(default = 1, null = False)
	
	def __str__(self):
		return f'book_ref:{self.book_ref} - book_date:{self.book_date}'

class Tickets(models.Model):
	ticket_no = models.AutoField(primary_key = True)
	book_ref = models.ForeignKey('Bookings', on_delete = models.CASCADE)
	passenger_id = models.CharField(max_length=32, null = False)
	passenger_name = models.CharField(max_length=64, null = False)
	contact_data = models.CharField(max_length=128, blank = True)
	
	def __str__(self):
		return f'ticket_number:{self.ticket_no} - passenger_name:{self.passenger_name}'

class Ticket_flights(models.Model):
	ticket_no = models.ForeignKey('Tickets', on_delete = models.CASCADE)
	flight_id = models.ForeignKey('Flights', on_delete = models.CASCADE)
	fare_conditions = models.ForeignKey('Seats', on_delete = models.CASCADE)
	amount = models.PositiveIntegerField(default = 1)
	
	class Meta:
		unique_together = (('ticket_no', 'flight_id'))
	
	def __str__(self):
		return f'ticket_number:{self.ticket_no} - fare_conditions:{self.fare_conditions}'

class Boarding_passes(models.Model):
	ticket_no = models.ForeignKey('Tickets', on_delete = models.CASCADE)
	flight_id = models.ForeignKey('Flights', on_delete = models.CASCADE)
	boarding_no = models.PositiveIntegerField(null = False)
	seat_no = models.ForeignKey('Seats', on_delete = models.CASCADE)
	
	class Meta:
		unique_together = (('ticket_no', 'flight_id'))
	
	def __str__(self):
		return f'ticket_number:{self.ticket_no} - seat_no:{self.seat_no}'


class Airports(models.Model):
	airport_code = models.CharField(max_length=3, primary_key = True, null = False)
	airport_name = models.CharField(max_length=128, null = False)
	city = models.CharField(max_length=128, null = False)
	coordinates = models.CharField(max_length=128, blank = True)
	timezone = models.CharField(max_length=12, blank = True)
	
	def __str__(self):
		return f'airport_code:{self.airport_code} - city:{self.city} - airport_name:{self.airport_name}'

class Aircrafts(models.Model):
	aircraft_code = models.CharField(max_length=32, primary_key = True, null = False)
	model = models.CharField(max_length=32)
	range = models.CharField(max_length=32, blank = True)
	
	def __str__(self):
		return f'aircraft_code:{self.aircraft_code} - model:{self.model}'

class Seats(models.Model):
	E = 'Эконом-класс'
	B = 'Бизнес-класс'
	FARE_CONDITIONS_CHOICES=[
	(E, 'Эконом'),
	(B, 'Бизнес-класс')
	]

	aircraft_code = models.ForeignKey('Aircrafts', on_delete = models.CASCADE)
	seat_no = models.CharField(max_length=3, null=False)
	fare_conditions = models.CharField(max_length=12, choices=FARE_CONDITIONS_CHOICES, default=E, null = False)
	
	class Meta:
		unique_together = (('aircraft_code', 'seat_no'))
	
	def __str__(self):
		return f'aircraft_code:{self.aircraft_code} - seat_no:{self.seat_no} - fare_conditions:{self.fare_conditions}'

class Flights(models.Model):
	schedule = 'вылет по расписанию'
	fly = 'летит'
	late = 'задерживается'
	land = 'приземлился'
	
	STATUS_CHOICES = [
	(schedule, 'вылет по расписанию'),
	(fly, 'летит'),
	(late, 'задерживается'),
	(land, 'приземлился')
	]
	
	flight_id = models.AutoField(primary_key = True)
	flight_no = models.PositiveIntegerField(null=False)
	scheduled_departure = models.DateTimeField()
	scheduled_arrival = models.DateTimeField()
	departure_airport = models.ForeignKey('Airports', related_name='departure_airport', on_delete = models.CASCADE)
	arrival_airport = models.ForeignKey('Airports', related_name='arrival_airport', on_delete = models.CASCADE)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=schedule, null = False)
	aircraft_code = models.ForeignKey('Aircrafts', on_delete = models.CASCADE)
	actual_departure = models.DateTimeField(blank = True)
	actual_arrival = models.DateTimeField(blank = True)
	
	def __str__(self):
		return f'flight_id:{self.flight_id} - departure_airport:{self.departure_airport} - arrival_airport:{self.arrival_airport} - status:{self.status} - actual_departure:{self.actual_departure}'