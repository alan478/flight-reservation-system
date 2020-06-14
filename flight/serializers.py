from rest_framework import serializers
from .models import Flight,Passanger,Reservation


class FlightSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields='__all__'
class PassangerSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=Passanger
        fields='__all__'
class ReservationSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields='__all__'
