from django.shortcuts import render
from flight.models import Flight,Passanger,Reservation
from flight.serializers import FlightSerilaizer,PassangerSerilaizer,ReservationSerilaizer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

class FlightViewSet(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FlightSerilaizer

class PassangerViewSet(viewsets.ModelViewSet):
    queryset=Passanger.objects.all()
    serializer_class=PassangerSerilaizer
class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerilaizer

@api_view(['POST'])
def save_reservation(request):
    flight=Flight.objects.get(id=request.data['flightId'])

    passanger=Passanger()
    passanger.firstName=request.data['firstName']
    passanger.lastName=request.data['lastName']
    passanger.middleName=request.data['middleName']
    passanger.email=request.data['email']
    passanger.phone=request.data['phone']

    reservation=Reservation()
    reservation.flight=flights
    reservation.passanger=passanger
    Reservation.save(reservation)

    return Response(status=status.HTTP_201_CREATED)

@api_view(['POST'])
def find_flights(request):
    flights=Flight.objects.filter(departureCity=request.data['departureCity'],arrivalCity=request.data['arrivalCity'],dateOfDeparture=request.data('dateOfDeparture'))
    serializers=FlightSerilaizer(flights,many=true)
    return Response(serializers.data)




# Create your views here.
