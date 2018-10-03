from django.db import models
from datetime import datetime

class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

    

class Driver(models.Model):
    department = models.ForeignKey(Department,verbose_name='list of departments', on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    licence = models.CharField(max_length=50)
    pin = models.CharField(max_length=50)
    phonenumber = models.IntegerField()

    def __str__(self):
        return self.firstname + " " + self.lastname 

class Vehicle(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    year_make = models.CharField(max_length=50)
    chassis = models.CharField(max_length = 30)
    purchase_price = models.FloatField()

    def __str__(self):
        return self.number

class Assignment(models.Model):
    driver = models.ForeignKey(Driver, verbose_name='list of drivers', on_delete=models.CASCADE)
    vehicle  = models.ForeignKey(Vehicle, verbose_name='list of vehicles', on_delete=models.CASCADE)
    destination = models.CharField(max_length = 50)
    departure = models.DateTimeField(default=datetime.now)
    arrival = models.DateTimeField(default=datetime.now, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.destination

class Service(models.Model):
    vehicle = models.ForeignKey(Vehicle, verbose_name='list of vehicles', on_delete=models.CASCADE)
    # selection option for minor, major, medium
    MINOR = 'MI'
    MEDIUM = 'ME'
    MAJOR = 'MA'
    SIZE_OF_PROBLEM = (
        (MINOR, 'Minor'),
        (MEDIUM, 'Medium'),
        (MAJOR, 'Major'),
    )
    details_of_service = models.CharField(
        max_length=2,
        choices = SIZE_OF_PROBLEM,
        default = MINOR,
        ) 
    comment = models.TextField()
    serviced_on = models.DateTimeField(default=datetime.now)
    scheduled_service = models.DateTimeField(default=datetime.now)
    cost = models.FloatField()

    def __str__(self):
        return self.details_of_service 

class Fuel(models.Model): 
    # generate a report of that particular month for that particular vehicle
    vehicle = models.ForeignKey(Vehicle, verbose_name='list of vehicles', on_delete=models.CASCADE)
    speedometer = models.IntegerField()
    litres = models.FloatField()
    cost = models.FloatField()
    reading_on = models.DateTimeField(default=datetime.now)
    

    def __str__(self):
        return self.last_reading

     

