from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *;
from .models import *;

# Generic API view to handle CRUD operations
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated for all API actions
def generic_api(model_class, serializer_class):
    @api_view(['GET', 'POST', 'PUT', 'DELETE'])
    def api(request, id=None):
        if request.method == 'GET':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    serializer = serializer_class(instance)
                    return Response(serializer.data)
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'}, status=404)
            else:
                instances = model_class.objects.all()
                serializer = serializer_class(instances, many=True)
                return Response(serializer.data)

        elif request.method == 'POST':
            serializer = serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)

        elif request.method == 'PUT':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    serializer = serializer_class(instance, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                    return Response(serializer.errors, status=400)
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'}, status=404)
            return Response({'message': 'ID is required for update'}, status=400)

        elif request.method == 'DELETE':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    instance.delete()
                    return Response({'message': 'Deleted successfully'}, status=204)
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'}, status=404)
            return Response({'message': 'ID is required for deletion'}, status=400)

        return Response({'message': 'Invalid method'}, status=405)

    return api

# API views for RentPayment and Maintenance
manage_rentpayment = generic_api(RentPayment, RentPaymentSerializer)
manage_maintenance = generic_api(Maintenance, MaintenanceSerializer)
manage_user = generic_api(User, UserSerializer)
manage_tenant = generic_api(User, TenantSerializer)
manage_property = generic_api(Property, PropertySerializer)
manage_booking = generic_api(Booking, BookingSerializer)
