from django.contrib import admin
from .models import User, Property, Tenant, PropertyTenant, RentPayment, Maintenance
from .models import Booking
admin.site.register(User)
admin.site.register(Property)
admin.site.register(Tenant)
admin.site.register(PropertyTenant)
admin.site.register(RentPayment)
admin.site.register(Maintenance)
admin.site.register(Booking)
