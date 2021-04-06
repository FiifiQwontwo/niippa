from rest_framework import serializers
from .models import *


class EventDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDate
        fields = ('event_start_date', 'event_end_date', 'second_proposed_date',)


class EventAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAttendance
        fields = ('id', 'event_name', 'event_date',)


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = (
            'id', 'name_of_organisation', 'email_of_organisation', 'phone_number', 'event_date', 'event_attendance',)


class IndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individual
        fields = ('id', 'name', 'index', 'phoneNumber',
                  'email', 'eventDate',)
