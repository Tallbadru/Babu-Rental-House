from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class User(models.Model):
    ROLE_CHOICES = [
        ('Owner', 'Owner'),
        ('Tenant', 'Tenant'),
    ]
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username 

class Property(models.Model):
    ROOM_STATUS_CHOICES = [
        ('Empty', 'Empty'),
        ('Booked', 'Booked'),
    ]
    
    room_no = models.CharField(max_length=50,default="Room 1")  # Room number
    status = models.CharField(max_length=10, choices=ROOM_STATUS_CHOICES, default='Empty')  # Status of the room
    type = models.CharField(max_length=100)  # Type of property
    price = models.DecimalField(max_digits=10, decimal_places=2, default=100000)  # Price of the property with default value 100000
   
    
    def __str__(self):
        return f"Room {self.room_no} ({self.type}) - {self.status}"

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    lease_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="bookings")
    status = models.CharField(max_length=20, default="Pending")
    booking_date = models.DateField()

    def __str__(self):
        return f"Booking for {self.property.room_no} - {self.status}"

# class PropertyTenant(models.Model):
#     property = models.ForeignKey(Property, on_delete=models.CASCADE)
#     tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.tenant.name} rents {self.property.address}"

class PropertyTenant(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

class RentPayment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Overdue', 'Overdue'),
    ]
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Payment {self.id} - {self.amount} by {self.tenant.name}"

class Maintenance(models.Model):
    STATUS_CHOICES = [
        ('Requested', 'Requested'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='maintenance_requests')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='maintenance_requests')
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Maintenance {self.id} "
