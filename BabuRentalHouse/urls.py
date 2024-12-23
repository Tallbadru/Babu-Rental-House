"""
URL configuration for BabuRentalHouse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path  # Remove the duplicate import
# from BabuRentalHouse import views
# from .views import RentPaymentMaintenanceView
# urlpatterns = [
#     path('admin/', admin.site.urls),
    
#     path('maintenance/', RentPaymentMaintenanceView.as_view(), {'model_name': 'maintenance'}, name='maintenance_list'),
    
# ]

# from django.contrib import admin
# from django.urls import path
# from myApp.views import RentPaymentMaintenanceView
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path(
#         'maintenance/',  RentPaymentMaintenanceView.as_view(),   {'model_name': 'maintenance'}, name='maintenance_list'
#     ),
# ]
from django.contrib import admin
from django.urls import path
from myApp.views import manage_rentpayment, manage_maintenance,manage_user ,manage_tenant, manage_property

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rentpayment/', manage_rentpayment),  # Handles RentPayment operations
    path('rentpayment/<int:id>/', manage_rentpayment),  # Handles specific RentPayment operations by ID
    path('maintenance/', manage_maintenance),  # Handles Maintenance operations
    path('maintenance/<int:id>/', manage_maintenance),  # Handles specific Maintenance operations by ID
    path('user/', manage_user),
    path('user/<int:id>/', manage_user),
    path('tenant/', manage_tenant),
    path('tenant/<int:id>/', manage_tenant),
    path('property/', manage_user),
    path('property/<int:id>/', manage_property),

]
