from django.contrib import admin

from .models import Department, Driver, Assignment, Vehicle, Service, Fuel

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("department", "firstname", "lastname", 'licence', 'pin', "phonenumber")

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'driver', 'destination', 'departure', 'arrival', 'description')

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'chassis', 'year_make', 'purchase_price')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'details_of_service', 'comment', 'serviced_on', 'scheduled_service', 'cost')

@admin.register(Fuel)
class FuelAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'speedometer', 'litres', 'reading_on', 'cost')

