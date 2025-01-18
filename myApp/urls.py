# from django.contrib import admin
# from myApp.views import manage_rentpayment, manage_maintenance, manage_user, manage_tenant, manage_property, manage_booking
# from django.urls import path
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

# urlpatterns = [
#     # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('admin/', admin.site.urls),
#     path('rentpayment/', manage_rentpayment),  # Handles RentPayment operations
#     path('rentpayment/<int:id>/', manage_rentpayment),  # Handles specific RentPayment operations by ID
#     path('maintenance/', manage_maintenance),  # Handles Maintenance operations
#     path('maintenance/<int:id>/', manage_maintenance),  # Handles specific Maintenance operations by ID
#     path('user/', manage_user),
#     path('user/<int:id>/', manage_user),
#     path('tenant/', manage_tenant),
#     path('tenant/<int:id>/', manage_tenant),
#     path('property/', manage_property),
#     path('property/<int:id>/', manage_property),
#     path('booking/', manage_booking),
#     path('booking/<int:id>/', manage_booking),
# ]
from myApp.views import manage_rentpayment, manage_maintenance, manage_user, manage_tenant, manage_property, manage_booking, LoginView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('rentpayment/', manage_rentpayment),  # Handles RentPayment operations
    path('rentpayment/<int:id>/', manage_rentpayment),  # Handles specific RentPayment operations by ID
    path('maintenance/', manage_maintenance),  # Handles Maintenance operations
    path('maintenance/<int:id>/', manage_maintenance),  # Handles specific Maintenance operations by ID
    path('user/', manage_user),
    path('user/<int:id>/', manage_user),
    path('tenant/', manage_tenant),
    path('tenant/<int:id>/', manage_tenant),
    path('property/', manage_property),
    path('property/<int:id>/', manage_property),
    path('booking/', manage_booking),
    path('booking/<int:id>/', manage_booking),
    path('login/', LoginView.as_view(), name='login'),
]