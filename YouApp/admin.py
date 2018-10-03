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
    pass

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    pass

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Fuel)
class FuelAdmin(admin.ModelAdmin):
    pass

